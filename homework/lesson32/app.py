import asyncio
import json
import os
from aiohttp import web
from dotenv import load_dotenv

# Importy specyficzne dla Async SQLAlchemy
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

# Importy znane z synchronicznego SQLAlchemy
from sqlalchemy import select
from sqlalchemy.orm import joinedload

# Importy lokalne
# Modele wydzielone po Task 19, aby uniknąć circular import
from models import Account, Base, Product, User
from routes import setup_routes



# --- USTAWIENIA BAZY DANYCH ---
load_dotenv()

DB_URL = os.environ.get(
    "DB_URL",
    "postgresql+asyncpg://postgres:postgres@localhost/aio_test_db"
)



# --- Kontekst Aplikacji (Startup / Cleanup) ---
async def init_db(app: web.Application):
    """Sygnał on_startup: tworzy silnik i sessionmaker."""
    print(f"Inicjalizuję połączenie z bazą danych: {DB_URL}")

    # 1. Tworzymy asynchroniczny silnik
    engine = create_async_engine(DB_URL, echo=True)

    # 2. Tworzymy fabrykę sesji (Session Maker)
    # W trybie async, sessionmaker tworzymy z `class_=AsyncSession`
    async_session_factory = async_sessionmaker(
        engine,
        expire_on_commit=False,  # Ważne dla async
        class_=AsyncSession
    )

    # 3. (Opcjonalnie) Stworzenie tabel przy starcie (tylko dla deweloperki!)
    async with engine.begin() as conn:
        # Używamy run_sync do uruchomienia synchronicznej metody create_all
        await conn.run_sync(Base.metadata.create_all)

    # 4. Przechowujemy silnik i fabrykę sesji w obiekcie aplikacji
    app["db_engine"] = engine
    app["db_session_factory"] = async_session_factory

    print("Połączenie z bazą danych gotowe.")


async def close_db(app: web.Application):
    """Sygnał on_cleanup: zamyka silnik."""
    print("Zamykam pulę połączeń z bazą danych.")
    await app["db_engine"].dispose()



# --- Handlery korzystające z Bazy Danych ---
async def create_user(request: web.Request) -> web.Response:
    try:
        data = await request.json()
        username = data["username"]
        email = data["email"]
    except (json.JSONDecodeError, KeyError, TypeError):
        raise web.HTTPBadRequest(text="Oczekiwano JSON z 'username' i 'email'.")

    # Pobieramy fabrykę sesji z aplikacji
    session_factory: async_sessionmaker[AsyncSession] = request.app["db_session_factory"]

    # Otwieramy nową sesję
    # `async with` zarządza `await session.close()`
    async with session_factory() as session:
        # `async with session.begin()` zarządza `await session.commit()` lub `await session.rollback()`
        async with session.begin():
            stmt_exists = select(User).where(User.username == username)
            existing_user = await session.execute(stmt_exists)

            if existing_user.scalar_one_or_none() is not None:
                raise web.HTTPConflict(text=f"Użytkownik {username} już istnieje")

            new_user = User(username=username, email=email)
            session.add(new_user)

            # Musimy `await session.flush()`, aby dostać ID przed commitem
            await session.flush()
            user_data = new_user.to_dict()

    return web.json_response(user_data, status=201)


async def get_users(request: web.Request) -> web.Response:
    session_factory: async_sessionmaker[AsyncSession] = request.app["db_session_factory"]

    async with session_factory() as session:
        # Tworzymy zapytanie (identycznie jak w sync SQLAlchemy 2.0)
        stmt = select(User)

        # Wykonujemy zapytanie z `await`
        result = await session.execute(stmt)

        # Pobieramy obiekty
        # .scalars() pobiera pierwszą kolumnę (nasze obiekty User)
        # .all() materializuje listę (również operacja I/O)
        users = result.scalars().all()

        users_data = [u.to_dict() for u in users]

    return web.json_response(users_data)


# Task 9 + 20 (challenge) - tworzenie produktu
async def create_product(request: web.Request) -> web.Response:
    try:
        data = await request.json()
        name = data["name"]
        price = data["price"]
        user_id = data["user_id"]
    except (json.JSONDecodeError, KeyError, TypeError):
        raise web.HTTPBadRequest(
            text="Oczekiwano JSON z 'name', 'price' i 'user_id'."
        )

    if not isinstance(name, str) or not name.strip():
        raise web.HTTPBadRequest(
            text="'name' musi być niepustym tekstem."
        )

    if len(name.strip()) > 100:
        raise web.HTTPBadRequest(
            text="'name' może mieć maksymalnie 100 znaków."
        )

    session_factory: async_sessionmaker[AsyncSession] = (
        request.app["db_session_factory"]
    )

    async with session_factory() as session:
        async with session.begin():
            user = await session.get(User, user_id)

            if user is None:
                raise web.HTTPNotFound(
                    text="Nie znaleziono użytkownika."
                )

            try:
                new_product = Product(
                    name=name.strip(),
                    price=price,
                    user_id=user_id
                )
            except ValueError as error:
                raise web.HTTPBadRequest(text=str(error))

            session.add(new_product)

            await session.flush()
            product_data = new_product.to_dict()

    return web.json_response(product_data, status=201)


# Task 10 + 17 (challenge) - lista produktów z paginacją
async def get_products(request: web.Request) -> web.Response:
    try:
        page = int(request.query.get("page", 1))
        limit = int(request.query.get("limit", 10))
    except ValueError:
        raise web.HTTPBadRequest(
            text="'page' i 'limit' muszą być liczbami całkowitymi."
        )

    if page < 1 or limit < 1:
        raise web.HTTPBadRequest(
            text="'page' i 'limit' muszą być większe od 0."
        )

    offset = (page - 1) * limit

    session_factory: async_sessionmaker[AsyncSession] = (
        request.app["db_session_factory"]
    )

    async with session_factory() as session:
        stmt = (
            select(Product)
            .order_by(Product.id)
            .offset(offset)
            .limit(limit)
        )

        result = await session.execute(stmt)
        products = result.scalars().all()
        products_data = [product.to_dict() for product in products]

    return web.json_response(products_data)


# Task 11 + 20 (challenge) - pobieranie produktu wraz z twórcą
async def get_product(request: web.Request) -> web.Response:
    try:
        product_id = int(request.match_info["id"])
    except ValueError:
        raise web.HTTPBadRequest(
            text="ID produktu musi być liczbą całkowitą."
        )

    session_factory: async_sessionmaker[AsyncSession] = (
        request.app["db_session_factory"]
    )

    async with session_factory() as session:
        stmt = (
            select(Product)
            .options(joinedload(Product.user))
            .where(Product.id == product_id)
        )

        result = await session.execute(stmt)
        product = result.scalar_one_or_none()

    if product is None:
        raise web.HTTPNotFound()

    product_data = product.to_dict()
    product_data["created_by"] = product.user.username

    return web.json_response(product_data)


# Task 14 (challenge) - aktualizacja produktu
async def update_product(request: web.Request) -> web.Response:
    try:
        product_id = int(request.match_info["id"])
    except ValueError:
        raise web.HTTPBadRequest(
            text="ID produktu musi być liczbą całkowitą."
        )

    try:
        data = await request.json()
    except json.JSONDecodeError:
        raise web.HTTPBadRequest(
            text="Oczekiwano poprawnego JSON."
        )

    if not isinstance(data, dict):
        raise web.HTTPBadRequest(
            text="Oczekiwano obiektu JSON."
        )

    if "name" not in data and "price" not in data:
        raise web.HTTPBadRequest(
            text="Podaj 'name' i/lub 'price'."
        )

    session_factory: async_sessionmaker[AsyncSession] = (
        request.app["db_session_factory"]
    )

    async with session_factory() as session:
        async with session.begin():
            stmt = select(Product).where(Product.id == product_id)
            result = await session.execute(stmt)

            product = result.scalar_one_or_none()

            if product is None:
                raise web.HTTPNotFound()

            if "name" in data:
                name = data["name"]

                if not isinstance(name, str) or not name.strip():
                    raise web.HTTPBadRequest(
                        text="'name' musi być niepustym tekstem."
                    )

                if len(name.strip()) > 100:
                    raise web.HTTPBadRequest(
                        text="'name' może mieć maksymalnie 100 znaków."
                    )

                product.name = name.strip()

            if "price" in data:
                try:
                    product.price = data["price"]
                except ValueError as error:
                    raise web.HTTPBadRequest(
                        text=str(error)
                    )

            product_data = product.to_dict()

    return web.json_response(product_data)


# Task 15 (challenge) - usuwanie produktu
async def delete_product(request: web.Request):
    try:
        product_id = int(request.match_info["id"])
    except ValueError:
        raise web.HTTPBadRequest(
            text="ID produktu musi być liczbą całkowitą."
        )

    session_factory: async_sessionmaker[AsyncSession] = (
        request.app["db_session_factory"]
    )

    async with session_factory() as session:
        async with session.begin():
            stmt = select(Product).where(Product.id == product_id)
            result = await session.execute(stmt)

            product = result.scalar_one_or_none()

            if product is None:
                raise web.HTTPNotFound()

            await session.delete(product)

    return web.Response(status=204)


# Task 16 (challenge) - transfer środków
async def transfer(request: web.Request) -> web.Response:
    try:
        data = await request.json()
        from_id = data["from_id"]
        to_id = data["to_id"]
        amount = data["amount"]
    except (json.JSONDecodeError, KeyError, TypeError):
        raise web.HTTPBadRequest(
            text="Oczekiwano JSON z 'from_id', 'to_id' i 'amount'."
        )

    if (
        isinstance(amount, bool)
        or not isinstance(amount, int)
        or amount <= 0
    ):
        raise web.HTTPBadRequest(
            text="'amount' musi być dodatnią liczbą całkowitą."
        )

    if from_id == to_id:
        raise web.HTTPBadRequest(
            text="Konta źródłowe i docelowe muszą być różne."
        )

    session_factory: async_sessionmaker[AsyncSession] = (
        request.app["db_session_factory"]
    )

    async with session_factory() as session:
        async with session.begin():
            stmt = (
                select(Account)
                .where(Account.id.in_([from_id, to_id]))
                .with_for_update()
            )

            result = await session.execute(stmt)
            accounts = {account.id: account for account in result.scalars()}

            from_account = accounts.get(from_id)
            to_account = accounts.get(to_id)

            if from_account is None or to_account is None:
                raise web.HTTPNotFound(
                    text="Nie znaleziono jednego z kont."
                )

            if from_account.balance < amount:
                raise web.HTTPBadRequest(
                    text="Niewystarczające środki."
                )

            from_account.balance -= amount
            to_account.balance += amount

    return web.json_response(
        {
            "from_id": from_id,
            "from_balance": from_account.balance,
            "to_id": to_id,
            "to_balance": to_account.balance,
            "amount": amount
        }
    )


# Task 18 (challenge) - mock API dla AI
async def mock_chat(request: web.Request) -> web.Response:
    try:
        data = await request.json()
        prompt_text = data["prompt"]
    except (json.JSONDecodeError, KeyError, TypeError):
        raise web.HTTPBadRequest(
            text="Oczekiwano poprawnego JSON z 'prompt'."
        )

    if not isinstance(prompt_text, str) or not prompt_text.strip():
        raise web.HTTPBadRequest(
            text="'prompt' musi być niepustym tekstem."
        )

    await asyncio.sleep(3)

    return web.json_response(
        {
            "response": (
                f"Otrzymałem twój prompt: '{prompt_text}' "
                "i przetworzyłem go."
            )
        }
    )



# --- Tworzenie Aplikacji ---
def create_app():
    app = web.Application()

    setup_routes(
        app,
        create_user,
        get_users,
        create_product,
        get_products,
        get_product,
        update_product,
        delete_product,
        transfer,
        mock_chat,
    )

    # Rejestrujemy sygnały
    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)

    return app



if __name__ == "__main__":
    app = create_app()

    print(f"--- Start serwera na [http://127.0.0.1:8080] (http://127.0.0.1:8080) ---")
    print(f"--- Upewnij się, że baza danych na {DB_URL} działa i jest utworzona. ---")

    web.run_app(app, port=8080)