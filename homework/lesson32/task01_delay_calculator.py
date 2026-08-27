import asyncio
import time


async def main() -> None:
    start = time.perf_counter()

    await asyncio.gather(
        asyncio.sleep(1),
        asyncio.sleep(4),
        asyncio.sleep(2),
    )

    execution_time = time.perf_counter() - start

    print(f"Całkowity czas wykonania: {execution_time:.2f} s")


if __name__ == "__main__":
    asyncio.run(main())