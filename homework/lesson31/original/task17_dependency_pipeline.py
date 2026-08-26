import asyncio
import time


async def pobierz_id_uzytkownika(nazwa_uzytkownika: str) -> int:
    await asyncio.sleep(1)
    return 42


async def pobierz_posty(id_uzytkownika: int) -> list[int]:
    await asyncio.sleep(1)
    return [101, 102, 103]


async def pobierz_komentarze(id_postu: int) -> list[str]:
    await asyncio.sleep(1)

    return [
        f"Komentarz 1 do posta {id_postu}",
        f"Komentarz 2 do posta {id_postu}",
    ]


async def main() -> None:
    nazwa_uzytkownika = "tomek"

    start = time.perf_counter()

    id_uzytkownika = await pobierz_id_uzytkownika(nazwa_uzytkownika)
    posty = await pobierz_posty(id_uzytkownika)

    komentarze = await asyncio.gather(
        *(pobierz_komentarze(id_postu) for id_postu in posty)
    )

    execution_time = time.perf_counter() - start

    print(f"Użytkownik: {nazwa_uzytkownika}")
    print(f"ID użytkownika: {id_uzytkownika}")
    print(f"Posty: {posty}")

    for id_postu, komentarze_postu in zip(posty, komentarze):
        print(f"\nPost {id_postu}:")

        for komentarz in komentarze_postu:
            print(f"- {komentarz}")

    print(f"\nCzas wykonania: {execution_time:.2f} s")


if __name__ == "__main__":
    asyncio.run(main())