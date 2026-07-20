import asyncio
import time

async def operacja(nazwa, czas_trwania):
    print(f"Start: {nazwa}")
    await asyncio.sleep(czas_trwania)
    print(f"Koniec: {nazwa}")
    return f"Wynik z {nazwa}"

async def main():
    start_time = time.time()
    
    # gather uruchamia wszystkie korutyny współbieżnie
    
    op_a = await asyncio.create_task(operacja("A", 3))
    op_b = await asyncio.create_task(operacja("B", 1))
    op_c = await asyncio.create_task(operacja("C", 2))
    
    print(op_a, op_b, op_c)
    time.sleep(3)
    print(op_a, op_b, op_c)
    # Czas wykonania: ~3s (czas najdłuższej operacji)
    
asyncio.run(main())