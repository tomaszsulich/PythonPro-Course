import asyncio
import json
import random
from datetime import datetime, timedelta, timezone

import aiohttp
import jwt
from aiohttp import web
from jwt.exceptions import InvalidTokenError


SECRET_KEY = "lesson34-websocket-jwt-secret-key"
ALGORITHM = "HS256"
BOARD_SIZE = 3

authenticated_connections: dict[web.WebSocketResponse, str] = {}
players: dict[web.WebSocketResponse, str] = {}

game_state = {
    "board": [
        [""] * BOARD_SIZE
        for _ in range(BOARD_SIZE)
    ],
    "current_player": "X",
    "winner": None,
}


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


def check_winner(board: list[list[str]]) -> str | None:
    for row in board:
        if row[0] and all(symbol == row[0] for symbol in row):
            return row[0]

    for column in range(BOARD_SIZE):
        symbol = board[0][column]

        if symbol and all(
            board[row][column] == symbol
            for row in range(BOARD_SIZE)
        ):
            return symbol

    symbol = board[0][0]

    if symbol and all(
        board[index][index] == symbol
        for index in range(BOARD_SIZE)
    ):
        return symbol

    symbol = board[0][BOARD_SIZE - 1]

    if symbol and all(
        board[index][BOARD_SIZE - 1 - index] == symbol
        for index in range(BOARD_SIZE)
    ):
        return symbol

    return None


def is_board_full(board: list[list[str]]) -> bool:
    return all(
        cell != ""
        for row in board
        for cell in row
    )


async def broadcast_state() -> None:
    for connection in players:
        if not connection.closed:
            await connection.send_json(game_state)


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

        if len(players) >= 2:
            await ws.send_str("❌ W tę grę mogą grać tylko dwie osoby.")
            await ws.close()
            return ws

        if not players:
            symbol = random.choice(("X", "O"))
        else:
            symbol = "O" if "X" in players.values() else "X"

        players[ws] = symbol

        print(f"👤 Użytkownik {user_id} gra jako {symbol}")

        await ws.send_json({
            "type": "player",
            "symbol": symbol,
        })

        await broadcast_state()

        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                try:
                    data = json.loads(msg.data)
                except json.JSONDecodeError:
                    await ws.send_str("❌ Nieprawidłowa wiadomość.")
                    continue

                row = data.get("row")
                column = data.get("column")

                if game_state["winner"] is not None:
                    await ws.send_str("❌ Gra została już zakończona.")
                    continue

                if players[ws] != game_state["current_player"]:
                    await ws.send_str("❌ Nie Twoja kolej.")
                    continue

                if not isinstance(row, int) or not isinstance(column, int):
                    await ws.send_str(
                        "❌ Wiersz i kolumna muszą być liczbami."
                    )
                    continue

                if not (0 <= row < BOARD_SIZE and 0 <= column < BOARD_SIZE):
                    await ws.send_str(
                        "❌ Pole znajduje się poza planszą."
                    )
                    continue

                if game_state["board"][row][column] != "":
                    await ws.send_str(
                        "❌ To pole zostało już wykorzystane."
                    )
                    continue

                game_state["board"][row][column] = players[ws]

                winner = check_winner(game_state["board"])

                if winner is not None:
                    game_state["winner"] = winner
                elif is_board_full(game_state["board"]):
                    game_state["winner"] = "draw"
                else:
                    game_state["current_player"] = (
                        "O"
                        if game_state["current_player"] == "X"
                        else "X"
                    )

                await broadcast_state()

            elif msg.type == web.WSMsgType.ERROR:
                print(f"❌ Błąd WebSocket: {ws.exception()}")

    finally:
        players.pop(ws, None)
        user_id = authenticated_connections.pop(ws, None)

        if user_id:
            print(f"❌ Użytkownik {user_id} rozłączony.")

    return ws


async def websocket_client(user_id: str, token: str,
                           moves: list[tuple[int, int]]) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect("ws://localhost:8080/ws") as ws:
            await ws.send_str(token)

            auth_response = await ws.receive()
            print(f"📥 Klient: {auth_response.data}")

            if auth_response.data != "✅ Uwierzytelniono.":
                return

            symbol = None
            player_moves: list[tuple[int, int]] = []
            move_index = 0
            move_sent = False

            async for msg in ws:
                if msg.type != web.WSMsgType.TEXT:
                    continue

                try:
                    payload = json.loads(msg.data)
                except json.JSONDecodeError:
                    print(f"📥 {user_id}: {msg.data}")
                    continue

                if payload.get("type") == "player":
                    symbol = payload["symbol"]
                    player_moves = moves[symbol]

                    print(f"👤 {user_id}: Grasz jako {symbol}")
                    continue

                print(f"📡 {user_id}: Stan gry: {payload}")

                if payload["winner"] is not None:
                    if payload["winner"] == "draw":
                        print(f"🤝 {user_id} ({symbol}): Ups, remis!")
                    elif payload["winner"] == symbol:
                        print(f"🏆 {user_id} ({symbol}): Wygrałeś!")
                    else:
                        print(f"😕 {user_id} ({symbol}): Przegrałeś!")

                    return

                if symbol != payload["current_player"]:
                    move_sent = False

                if (
                    symbol == payload["current_player"]
                    and not move_sent
                    and move_index < len(player_moves)
                ):
                    row, column = player_moves[move_index]
                    move_index += 1
                    move_sent = True

                    await ws.send_json({
                        "row": row,
                        "column": column,
                    })


async def main() -> None:
    app = web.Application()
    app.router.add_get("/ws", websocket_handler)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "localhost", 8080)
    await site.start()

    print("📡 Serwer działa na ws://localhost:8080/ws")

    token_player_1 = create_token("player_1")
    token_player_2 = create_token("player_2")

    win_moves = {
        "X": [
            (0, 0),
            (0, 1),
            (0, 2),
        ],
        "O": [
            (1, 0),
            (1, 1),
        ],
    }

    draw_moves = {
        "X": [
            (0, 0),
            (0, 2),
            (1, 0),
            (2, 1),
            (2, 2),
        ],
        "O": [
            (0, 1),
            (1, 1),
            (1, 2),
            (2, 0),
        ],
    }

    await asyncio.gather(
        websocket_client("player_1", token_player_1, draw_moves),
        websocket_client("player_2", token_player_2, draw_moves),
    )

    await runner.cleanup()


if __name__ == "__main__":
    asyncio.run(main())