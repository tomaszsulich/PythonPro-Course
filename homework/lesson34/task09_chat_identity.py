from aiohttp import web
from time import perf_counter


active_connections: set[web.WebSocketResponse] = set()


async def broadcast_message(message: str,
                            sender: web.WebSocketResponse | None = None) -> None:
    for connection in active_connections:
        if connection != sender and not connection.closed:
            try:
                await connection.send_str(message)
            except Exception as e:
                print(f"❌ Błąd wysyłania do klienta: {e}")


async def chat_handler(request: web.Request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    connection_start = perf_counter()

    active_connections.add(ws)
    print(f"✅ Nowy klient! Łącznie połączeń: {len(active_connections)}")

    await broadcast_message(
        f"🟢 Nowy użytkownik dołączył! Aktywnych: {len(active_connections)}",
        sender=ws,
    )

    try:
        nickname_msg = await ws.receive()

        if nickname_msg.type != web.WSMsgType.TEXT:
            return ws

        nickname = nickname_msg.data

        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                await broadcast_message(
                    f"💬 {nickname}: {msg.data}",
                    sender=ws,
                )

            elif msg.type == web.WSMsgType.ERROR:
                print(f"❌ Błąd WebSocket: {ws.exception()}")

    finally:
        connection_time = perf_counter() - connection_start
        active_connections.discard(ws)

        print(f"⏱️ Czas połączenia: {connection_time:.2f} s")
        print(f"❌ Klient rozłączony. Zostało: {len(active_connections)}")

        await broadcast_message(
            f"🔴 Użytkownik opuścił chat. Aktywnych: {len(active_connections)}"
        )

    return ws


app = web.Application()
app.router.add_get("/chat", chat_handler)


if __name__ == "__main__":
    print("🚀 Chat server działa na ws://localhost:8080/chat")
    web.run_app(app, host="localhost", port=8080)