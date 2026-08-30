import os
from datetime import datetime

from aiohttp import web
from dotenv import load_dotenv
from sqlalchemy import DateTime, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite+aiosqlite:///chat.db",
)

engine = create_async_engine(DATABASE_URL)
session_factory = async_sessionmaker(engine, expire_on_commit=False)

active_connections: set[web.WebSocketResponse] = set()


class Base(DeclarativeBase):
    pass


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
    )


async def create_tables() -> None:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


async def save_message(content: str) -> None:
    async with session_factory() as session:
        message = Message(content=content)
        session.add(message)
        await session.commit()


async def get_last_messages(limit: int = 50) -> list[Message]:
    async with session_factory() as session:
        result = await session.execute(
            select(Message)
            .order_by(Message.id.desc())
            .limit(limit)
        )

        messages = list(result.scalars())
        messages.reverse()

        return messages


async def broadcast_message(message: str,
                            sender: web.WebSocketResponse | None = None) -> None:
    for connection in active_connections:
        if connection != sender and not connection.closed():
            try:
                await connection.send_str(message)
            except Exception as e:
                print(f"❌ Błąd wysyłania do klienta: {e}")


async def chat_handler(request: web.Request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    active_connections.add(ws)
    print(f"✅ Nowy klient! Łącznie połączeń: {len(active_connections)}")

    try:
        history = await get_last_messages()

        for message in history:
            await ws.send_str(f"📜 {message.content}")

        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                await save_message(msg.data)

                await broadcast_message(
                    msg.data,
                    sender=ws,
                )

            elif msg.type == web.WSMsgType.ERROR:
                print(f"❌ Błąd WebSocket: {ws.exception()}")

    finally:
        active_connections.discard(ws)
        print(f"❌ Klient rozłączony. Zostało: {len(active_connections)}")

    return ws


async def on_startup(app: web.Application) -> None:
    await create_tables()

    database = (
        "PostgreSQL"
        if DATABASE_URL.startswith("postgresql")
        else "SQLite"
    )
    print(f"🗄️ Baza danych: {database}")


async def on_cleanup(app: web.Application) -> None:
    await engine.dispose()


app = web.Application()
app.router.add_get("/chat", chat_handler)

app.on_startup.append(on_startup)
app.on_cleanup.append(on_cleanup)


if __name__ == "__main__":
    print("🚀 Chat server działa na ws://localhost:8080/chat")
    web.run_app(app, host="localhost", port=8080)