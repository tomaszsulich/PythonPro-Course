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
            if msg.type == web.WSMsgType.TEXT:
                print(f"📥 {user_id}: {msg.data}")

                await ws.send_str(
                    f"Server: {msg.data}"
                )

            elif msg.type == web.WSMsgType.ERROR:
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

            messages = [
                "Pierwsza wiadomość.",
                "Druga wiadomość.",
            ]

            for message in messages:
                await ws.send_str(message)
                print(f"📤 Klient wysłał: {message}")

                response = await ws.receive()
                print(f"📥 Klient otrzymał: {response.data}")


async def main() -> None:
    app = web.Application()
    app.router.add_get("/ws", websocket_handler)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "localhost", 8080)
    await site.start()

    print("🚀 WebSocket działa na ws://localhost:8080/ws")

    token = create_token("user_1")

    try:
        await websocket_client(token)
    finally:
        await runner.cleanup()


if __name__ == "__main__":
    asyncio.run(main())