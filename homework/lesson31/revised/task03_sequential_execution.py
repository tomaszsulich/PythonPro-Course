import asyncio


# Nazwy funkcji zgodne z treścią zadania.
async def zadanie1() -> None:
    await asyncio.sleep(2)
    print("Zadanie 1 zakończone")


async def zadanie2() -> None:
    await asyncio.sleep(1)
    print("Zadanie 2 zakończone")


async def main() -> None:
    await zadanie1()
    await zadanie2()


if __name__ == "__main__":
    asyncio.run(main())