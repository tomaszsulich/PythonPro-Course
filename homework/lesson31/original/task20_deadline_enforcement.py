import asyncio
import random


TIMEOUT = 3


async def delayed_task() -> int:
    delay = random.randint(1, 5)
    await asyncio.sleep(delay)
    return delay


async def main() -> None:
    try:
        delay = await asyncio.wait_for(
            delayed_task(),
            timeout=TIMEOUT,
        )
        print(f"Zadanie zakończone po {delay} s.")
    except asyncio.TimeoutError:
        print(
            f"Przekroczono limit {TIMEOUT} s. "
            "Zadanie zostało anulowane."
        )


if __name__ == "__main__":
    asyncio.run(main())