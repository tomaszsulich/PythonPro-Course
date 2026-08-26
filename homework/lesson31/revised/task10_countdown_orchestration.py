import asyncio


async def countdown(name: str, start: int) -> None:
    for seconds_left in range(start, 0, -1):
        print(f"{name}: zostało {seconds_left} sekund")
        await asyncio.sleep(1)


async def main() -> None:
    await asyncio.gather(
        countdown("A", 5),
        countdown("B", 3),
        countdown("C", 7),
    )


if __name__ == "__main__":
    asyncio.run(main())