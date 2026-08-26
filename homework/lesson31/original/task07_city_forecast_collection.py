import asyncio
import random


# Nazwa funkcji i parametru zgodna z treścią zadania.
async def pobierz_pogode(miasto: str) -> dict[str, str | int]:
    await asyncio.sleep(1.5)

    return {
        "miasto": miasto,
        "temperatura": random.randint(15, 30),
        "stan": random.choice(
            ["słonecznie", "pochmurno", "deszczowo"],
        ),
    }


async def main() -> None:
    miasta = ["Warszawa", "Kraków", "Gdańsk"]

    wyniki = await asyncio.gather(
        *(pobierz_pogode(miasto) for miasto in miasta)
    )

    for wynik in wyniki:
        print(f"Miasto: {wynik['miasto']}")
        print(f"Temperatura: {wynik['temperatura']}°C")
        print(f"Stan: {wynik['stan']}")
        print()


if __name__ == "__main__":
    asyncio.run(main())