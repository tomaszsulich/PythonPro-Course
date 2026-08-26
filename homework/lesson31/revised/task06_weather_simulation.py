import asyncio


# Nazwa funkcji i parametru zgodna z treścią zadania.
async def pobierz_pogode(miasto: str) -> dict[str, str | int]:
    await asyncio.sleep(1.5)

    return {
        "miasto": miasto,
        "temperatura": 25,
        "stan": "słonecznie",
    }


async def main() -> None:
    pogoda = await pobierz_pogode("Warszawa")

    print(f"Miasto: {pogoda['miasto']}")
    print(f"Temperatura: {pogoda['temperatura']}°C")
    print(f"Stan: {pogoda['stan']}")


if __name__ == "__main__":
    asyncio.run(main())