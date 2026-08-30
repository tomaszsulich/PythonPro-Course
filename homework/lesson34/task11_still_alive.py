import asyncio
from time import perf_counter

import aiohttp
from aiohttp import web


async def websocket_handler(request: web.Request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    last_pong = perf_counter()

    async def ping_client() -> None:
        while not ws.closed:
            await asyncio.sleep(30)

            if perf_counter() - last_pong >= 60:
                print("❌ Brak odpowiedzi przez 60 s. Rozłączam klienta.")
                await ws.close()
                break

            await ws.send_str("ping")
            print("📤 Serwer wysłał: ping")

    ping_task = asyncio.create_task(ping_client())

    try:
        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT and msg.data == "pong":
                last_pong = perf_counter()
                print("📥 Serwer otrzymał: pong")

            elif msg.type == web.WSMsgType.ERROR:
                print(f"❌ Błąd WebSocket: {ws.exception()}")

    finally:
        ping_task.cancel()

        try:
            await ping_task
        except asyncio.CancelledError:
            pass

        print("❌ Klient rozłączony.")

    return ws


async def websocket_client() -> None:
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect("ws://localhost:8080/ws") as ws:
            print("✅ Klient połączony!")

            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT and msg.data == "ping":
                    print("📥 Klient otrzymał: ping")
                    await ws.send_str("pong")
                    print("📤 Klient wysłał: pong")


async def main() -> None:
    app = web.Application()
    app.router.add_get("/ws", websocket_handler)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "localhost", 8080)
    await site.start()

    print("🚀 WebSocket działa na ws://localhost:8080/ws")

    try:
        await websocket_client()
    finally:
        await runner.cleanup()


if __name__ == "__main__":
    asyncio.run(main())