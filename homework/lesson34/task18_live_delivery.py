import asyncio
from datetime import datetime, timedelta, timezone

import aiohttp
import jwt
from aiohttp import web
from jwt.exceptions import InvalidTokenError


SECRET_KEY = "lesson34-websocket-jwt-secret-key"
ALGORITHM = "HS256"

authenticated_connections: dict[web.WebSocketResponse, str] = {}


def create_token(user_id: str) -> str:
    payload = {
        "sub": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=5),
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str) -> str | None:
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )
    except InvalidTokenError:
        return None

    return payload.get("sub")


async def send_notification(notification: str,
                            user_id: str) -> None:
    for connection, connected_user_id in authenticated_connections.items():
        if connected_user_id == user_id and not connection.closed:
            try:
                await connection.send_str(notification)
            except Exception as e:
                print(f"❌ Błąd wysyłania do klienta: {e}")


async def notification_handler(request: web.Request) -> web.Response:
    data = await request.json()

    user_id = data.get("user_id")
    message = data.get("message")

    if not user_id or not message:
        return web.json_response(
            {"error": "user_id i message są wymagane."},
            status=400,
        )

    await send_notification(message, user_id)

    return web.json_response(
        {
            "user_id": user_id,
            "message": message,
        },
        status=201,
    )


async def websocket_handler(request: web.Request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    try:
        token_msg = await ws.receive()

        if token_msg.type != web.WSMsgType.TEXT:
            await ws.close()
            return ws

        user_id = verify_token(token_msg.data)

        if user_id is None:
            await ws.send_str("❌ Nieprawidłowy token.")
            await ws.close()
            return ws

        authenticated_connections[ws] = user_id

        print(f"✅ Uwierzytelniono użytkownika: {user_id}")
        await ws.send_str("✅ Uwierzytelniono.")

        async for msg in ws:
            if msg.type == web.WSMsgType.ERROR:
                print(f"❌ Błąd WebSocket: {ws.exception()}")

    finally:
        user_id = authenticated_connections.pop(ws, None)

        if user_id:
            print(f"❌ Użytkownik {user_id} rozłączony.")

    return ws


async def websocket_client(token: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect("ws://localhost:8080/ws") as ws:
            await ws.send_str(token)

            auth_response = await ws.receive()
            print(f"📥 Klient: {auth_response.data}")

            if auth_response.data != "✅ Uwierzytelniono.":
                return

            async for msg in ws:
                if msg.type == web.WSMsgType.TEXT:
                    print(f"🔔 Powiadomienie: {msg.data}")


async def create_test_notification() -> None:
    await asyncio.sleep(0.5)

    url = "http://localhost:8080/notifications"
    payload = {
        "user_id": "user_1",
        "message": "Stół numer 3 zakończył grę.",
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            print(f"📤 REST: {await response.json()}")


async def main() -> None:
    app = web.Application()
    app.router.add_post("/notifications", notification_handler)
    app.router.add_get("/ws", websocket_handler)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "localhost", 8080)
    await site.start()

    print("🚀 Serwer działa na http://localhost:8080")

    token = create_token("user_1")

    client_task = asyncio.create_task(
        websocket_client(token)
    )

    try:
        await create_test_notification()
        await asyncio.sleep(0.5)
    finally:
        client_task.cancel()
        await runner.cleanup()


if __name__ == "__main__":
    asyncio.run(main())