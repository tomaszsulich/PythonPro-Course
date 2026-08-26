import asyncio
from collections.abc import AsyncGenerator


async def generate_messages() -> AsyncGenerator[str]:
    messages = [
        "Połączono z usługą.",
        "Pobrano nowe dane.",
        "Przetwarzanie zakończone.",
        "Strumień został zamknięty.",
    ]

    for message in messages:
        await asyncio.sleep(0.5)
        yield message


async def main() -> None:
    async for message in generate_messages():
        print(message)


if __name__ == "__main__":
    asyncio.run(main())