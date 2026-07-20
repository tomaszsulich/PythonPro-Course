import asyncio
import time

async def przygotuj_danie(nazwa, czas_przygotowania):
    print(f"Rozpoczynam przygotowanie: {nazwa}")
    # Symulacja operacji I/O (np. czekanie na ugotowanie)
    # asyncio.sleep jest asynchroniczną wersją time.sleep()
    await asyncio.sleep(czas_przygotowania)
    print(f"Danie gotowe: {nazwa}")
    return f"Serwuję {nazwa}"

async def main():
    wynik = await przygotuj_danie("Pizza", 2)
    print(wynik)
    
# Uruchomienie głównej korutyny 'main'
asyncio.run(main())