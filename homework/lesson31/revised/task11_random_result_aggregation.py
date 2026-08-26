import asyncio
import random


async def generate_result() -> int:
    await asyncio.sleep(random.uniform(2, 5))
    return random.randint(1, 100)


async def main() -> None:
    results = await asyncio.gather(
        *(generate_result() for _ in range(10))
    )

    print(f"Wyniki: {results}")
    print(f"Suma wyników: {sum(results)}")


if __name__ == "__main__":
    asyncio.run(main())