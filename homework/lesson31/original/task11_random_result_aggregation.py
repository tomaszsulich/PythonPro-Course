import asyncio
import random


# Nazwa funkcji zgodna z treścią zadania.
async def dlugie_obliczenia() -> int:
    await asyncio.sleep(random.uniform(2, 5))
    return random.randint(1, 100)


async def main() -> None:
    results = await asyncio.gather(
        *(dlugie_obliczenia() for _ in range(10))
    )

    total = sum(results)

    print(f"Wyniki: {results}")
    print(f"Suma wyników: {total}")


if __name__ == "__main__":
    asyncio.run(main())