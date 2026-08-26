import asyncio


HOST = "localhost"
PORT = 8888


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    data = await reader.read(1024)
    message = data.decode()

    print(f"Odebrano: {message}")

    writer.write(data)
    await writer.drain()

    writer.close()
    await writer.wait_closed()


async def main() -> None:
    server = await asyncio.start_server(
        handle_client,
        HOST,
        PORT,
    )

    print(f"Serwer działa na {HOST}:{PORT}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nSerwer zatrzymany.")