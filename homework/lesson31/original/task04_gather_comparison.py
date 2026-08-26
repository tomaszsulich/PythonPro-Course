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

    sequential_time = time.perf_counter() - start

    start = time.perf_counter()

    await asyncio.gather(
        zadanie1(),
        zadanie2(),
    )

    concurrent_time = time.perf_counter() - start
    speedup = sequential_time / concurrent_time

    print(f"Sekwencyjnie: {sequential_time:.2f} s")
    print(f"Współbieżnie: {concurrent_time:.2f} s")
    print(f"Przyspieszenie: {speedup:.2f}×")


if __name__ == "__main__":
    asyncio.run(main())