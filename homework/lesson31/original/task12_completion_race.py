import asyncio
import random


async def delayed_result() -> int:
    delay = random.randint(1, 10)
    await asyncio.sleep(delay)
    return delay


async def main() -> None:
    tasks = [
        asyncio.create_task(delayed_result())
        for _ in range(5)
    ]

    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED,
    )

    winner = done.pop()
    print(f"Pierwsze zadanie zakończyło się po {winner.result()} s.")

    for task in pending:
        task.cancel()

    await asyncio.gather(*pending, return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main())