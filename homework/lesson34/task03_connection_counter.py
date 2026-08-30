from aiohttp import web


active_connections = 0


async def websocket_handler(request: web.Request):
    global active_connections

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    active_connections += 1
    client_number = active_connections

    print("✅ Nowy klient połączony!")
    await ws.send_str(f"Jesteś klientem numer {client_number}")

    try:
        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                print(f"📥 Otrzymano: {msg.data}")

                await ws.send_str(f"Server: {msg.data}")

            elif msg.type == web.WSMsgType.ERROR:
                print(f"❌ Błąd WebSocket: {ws.exception()}")

    finally:
        active_connections -= 1
        print("❌ Klient rozłączony!")

    return ws


app = web.Application()

app.router.add_get("/ws", websocket_handler)


if __name__ == "__main__":
    print("🚀 Serwer WebSocket działa na ws://localhost:8080/ws")
    web.run_app(app, host="localhost", port=8080)