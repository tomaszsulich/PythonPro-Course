import asyncio


# Nazwa funkcji, parametrów i zmiennej zgodna z treścią zadania.
async def odliczanie(nazwa: str, start: int) -> None:
    for pozostalo in range(start, 0, -1):
        print(f"{nazwa}: zostało {pozostalo} sekund")
        await asyncio.sleep(1)


async def main() -> None:
    await asyncio.gather(
        odliczanie("Odliczanie 1", 5),
        odliczanie("Odliczanie 2", 3),
        odliczanie("Odliczanie 3", 7),
    )


if __name__ == "__main__":
    asyncio.run(main())