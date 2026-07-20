import asyncio
import time

async def pobierz_dane_uzytkownika(user_id):
    print(f"Pobieram dane dla użytkownika {user_id}...")
    await asyncio.sleep(2)
    print("Dane użytkownika pobrane.")
    return {"id": user_id, "name": "Jan Kowalski"}

async def pobierz_zamowienia_uzytkownika(user_id):
    print(f"Pobieram zamówienia dla użytkownika {user_id}...")
    await asyncio.sleep(3)
    print("Zamówienia pobrane.")
    return ["książka", "długopis", "zeszyt"]


async def main():
    co_lst = [pobierz_dane_uzytkownika(1), pobierz_dane_uzytkownika(2)]
    task_lst = []
    async with asyncio.TaskGroup() as tg:
        for c in co_lst:
            task_lst.append(tg.create_task(c))
    print([t.result() for t in task_lst])
    
asyncio.run(main())