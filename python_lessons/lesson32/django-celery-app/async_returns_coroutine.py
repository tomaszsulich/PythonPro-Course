import asyncio

async def pobierz_dane_uzytkownika(user_id):
    print(f"Pobieram dane dla użytkownika {user_id}...")
    # Symulacja zapytania do bazy danych
    await asyncio.sleep(2)
    print("Dane użytkownika pobrane.")
    return {"id": user_id, "name": "Jan Kowalski"}

print("PRINT:", pobierz_dane_uzytkownika(10))