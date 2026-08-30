from aiohttp import web
from time import perf_counter


active_connections: set[web.WebSocketResponse] = set()
rooms: dict[str, set[web.WebSocketResponse]] = {}


async def broadcast_message(message: str, room: str,
                            sender: web.WebSocketResponse | None = None) -> None:
    for connection in rooms.get(room, set()):
        if connection != sender and not connection.closed:
            try:
                await connection.send_str(message)
            except Exception as e:
                print(f"❌ Błąd wysyłania do klienta: {e}")


def leave_room(ws: web.WebSocketResponse, room: str | None) -> None:
    if room is None:
        return

    room_connections = rooms.get(room)

    if room_connections is None:
        return

    room_connections.discard(ws)

    if not room_connections:
        del rooms[room]


async def chat_handler(request: web.Request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    connection_start = perf_counter()
    current_room: str | None = None

    active_connections.add(ws)
    print(f"✅ Nowy klient! Łącznie połączeń: {len(active_connections)}")

    try:
        nickname_msg = await ws.receive()

        if nickname_msg.type != web.WSMsgType.TEXT:
            return ws

        nickname = nickname_msg.data

        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                if msg.data.startswith("/join "):
                    room_name = msg.data.removeprefix("/join ").strip()

                    if not room_name:
                        await ws.send_str("❌ Podaj nazwę pokoju.")
                        continue

                    if current_room == room_name:
                        await ws.send_str(
                            f"ℹ️ Jesteś już w pokoju: {room_name}"
                        )
                        continue

                    leave_room(ws, current_room)

                    rooms.setdefault(room_name, set()).add(ws)
                    current_room = room_name

                    print(f"🚪 {nickname} dołączył do pokoju: {current_room}")

                    await ws.send_str(
                        f"✅ Dołączono do pokoju: {current_room}"
                    )

                    await broadcast_message(
                        f"🟢 {nickname} dołączył do pokoju.",
                        current_room,
                        sender=ws,
                    )

                    continue

                if current_room is None:
                    await ws.send_str(
                        "❌ Najpierw dołącz do pokoju przez /join nazwa."
                    )
                    continue

                await broadcast_message(
                    f"💬 {nickname}: {msg.data}",
                    current_room,
                    sender=ws,
                )

            elif msg.type == web.WSMsgType.ERROR:
                print(f"❌ Błąd WebSocket: {ws.exception()}")

    finally:
        connection_time = perf_counter() - connection_start

        active_connections.discard(ws)

        if current_room:
            await broadcast_message(
                f"🔴 {nickname} opuścił pokój.",
                current_room,
                sender=ws,
            )

        leave_room(ws, current_room)

        print(f"⏱️ Czas połączenia: {connection_time:.2f} s")
        print(f"❌ Klient rozłączony. Zostało: {len(active_connections)}")

    return ws


app = web.Application()
app.router.add_get("/chat", chat_handler)


if __name__ == "__main__":
    print("🚀 Chat server działa na ws://localhost:8080/chat")
    web.run_app(app, host="localhost", port=8080)