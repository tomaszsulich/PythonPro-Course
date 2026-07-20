import asyncio
import time

async def operacja(nazwa, czas_trwania):
    print(f"Start: {nazwa}")
    if czas_trwania == 2:
        raise Exception("exc")
    await asyncio.sleep(czas_trwania)
    print(f"Koniec: {nazwa}")
    return f"Wynik z {nazwa}"

async def main():
    start_time = time.time()
    
    # gather uruchamia wszystkie korutyny współbieżnie
    wyniki = await asyncio.gather(
        operacja("A", 3),
        operacja("B", 1),
        operacja("C", 2),
        return_exceptions=True, #<= zwraca wyjątek w postaci obiektu
    )
    
    print(f"Wyniki: {wyniki}")
    
    end_time = time.time()
    print(f"Całkowity czas wykonania: {end_time - start_time:.2f}s")
    # Czas wykonania: ~3s (czas najdłuższej operacji)
    
asyncio.run(main())