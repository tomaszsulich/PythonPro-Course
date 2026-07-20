import asyncio

# Definicja korutyny za pomocą 'async def'
async def moja_korutyna():
    print("Witaj w świecie asynchroniczności!")
    
# Wywołanie funkcji nie uruchamia jej, tylko tworzy obiekt korutyny
korutyna_obj = moja_korutyna()
print(f"Typ obiektu: {type(korutyna_obj)}")
print(f"Obiekt korutyny: {korutyna_obj}")

# Aby uruchomić korutynę, używamy asyncio.run()
print("Uruchamiam korutynę...")
asyncio.run(korutyna_obj)