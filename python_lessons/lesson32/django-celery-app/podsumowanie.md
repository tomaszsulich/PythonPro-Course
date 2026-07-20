
Korutyna:
    asynchroniczny "schemat" czynności
    `async def coroutine_name()`

Future:
    - wskaznik na wynik korutyny
    - praktycznie niewykorzystywany

Task:
    - "opakowana korutyna" zarejestrowana w event loop
    - musimy ją uruchomić przy uzyciu `await`
    - po wykonaniu uzyskujemy wynik

Event loop:
    - mechanizm zarzadzajacy programem asynchronicznym


URUCHAMIANIE KODU ASYNCHRONICZNEGO


async def main(): ...
asyncio.run(main())

await asyncio.gather(func(0), func(1))