import asyncio
import random


async def delayed_task() -> float:
    delay = random.uniform(1, 5)
    await asyncio.sleep(delay)
    return delay


async def main() -> None:
    try:
        delay = await asyncio.wait_for(
            delayed_task(),
            timeout=3,
        )
        print(f"Zadanie zakończone po {delay:.2f} s.")
    except asyncio.TimeoutError:
        print("Przekroczono limit czasu wynoszący 3 s.")


if __name__ == "__main__":
    asyncio.run(main())