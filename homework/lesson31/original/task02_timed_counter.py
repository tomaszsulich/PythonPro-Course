import asyncio


# Nazwa funkcji i parametru zgodna z treścią zadania.
async def licznik(n: int) -> None:
    for number in range(1, n + 1):
        await asyncio.sleep(1)
        print(number)


if __name__ == "__main__":
    asyncio.run(licznik(5))