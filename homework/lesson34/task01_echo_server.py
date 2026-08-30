from aiohttp import web


async def websocket_handler(request: web.Request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    print("✅ Nowy klient połączony!")

    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT:
            print(f"📥 Otrzymano: {msg.data}")

            await ws.send_str(f"Server: {msg.data}")

        elif msg.type == web.WSMsgType.ERROR:
            print(f"❌ Błąd WebSocket: {ws.exception()}")

    print("❌ Klient rozłączony!")
    return ws


app = web.Application()

app.router.add_get("/ws", websocket_handler)


if __name__ == "__main__":
    print("🚀 Serwer WebSocket działa na ws://localhost:8080/ws")
    web.run_app(app, host="localhost", port=8080)