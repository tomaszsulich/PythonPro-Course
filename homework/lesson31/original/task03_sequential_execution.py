import asyncio
import time


# Nazwy funkcji zgodne z treścią zadania.
async def zadanie1() -> None:
    await asyncio.sleep(2)
    print("Zadanie 1 zakończone")


async def zadanie2() -> None:
    await asyncio.sleep(1)
    print("Zadanie 2 zakończone")


async def main() -> None:
    start = time.perf_counter()

    await zadanie1()
    await zadanie2()

    execution_time = time.perf_counter() - start

    print(f"Czas wykonania: {execution_time:.2f} s")


if __name__ == "__main__":
    asyncio.run(main())