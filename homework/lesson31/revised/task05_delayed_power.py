import asyncio


# Nazwy funkcji i parametrów zgodne z treścią zadania.
async def oblicz_potege(liczba: int | float, potega: int) -> int | float:
    await asyncio.sleep(2)
    return liczba ** potega


async def main() -> None:
    wynik = await oblicz_potege(2, 3)
    print(f"Wynik: {wynik}")


if __name__ == "__main__":
    asyncio.run(main())