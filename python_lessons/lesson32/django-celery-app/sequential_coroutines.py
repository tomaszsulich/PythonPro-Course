import asyncio

async def pobierz_dane_uzytkownika(user_id):
    print(f"Pobieram dane dla użytkownika {user_id}...")
    # Symulacja zapytania do bazy danych
    await asyncio.sleep(2)
    print("Dane użytkownika pobrane.")
    return {"id": user_id, "name": "Jan Kowalski"}

async def pobierz_zamowienia_uzytkownika(user_id):
    print(f"Pobieram zamówienia dla użytkownika {user_id}...")
    # Symulacja zapytania do API
    await asyncio.sleep(3)
    print("Zamówienia pobrane.")
    return ["książka", "długopis", "zeszyt"]

async def main():
    # Uruchamiamy korutyny jedna po drugiej (sekwencyjnie)
    dane = await pobierz_dane_uzytkownika(1)
    zamowienia = await pobierz_zamowienia_uzytkownika(dane["id"])
    print(f"Użytkownik: {dane['name']}, zamówienia: {zamowienia}")
    # Całkowity czas wykonania: 2s + 3s = ~5s
    
asyncio.run(main())