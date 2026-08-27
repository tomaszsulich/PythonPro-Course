import aiohttp
import asyncio


async def fetch(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.json()


async def main() -> None:
    # Endpoint podany w zadaniu jest niedostępny.
    # Wersja poprawiona korzysta z trzech działających publicznych API
    # i, zgodnie z treścią zadania, z trzech różnych adresów URL.
    urls = [
        "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd",
        "https://api.frankfurter.dev/v2/rate/EUR/USD",
        "https://xaus.com/api/v1/spot",
    ]

    async with aiohttp.ClientSession() as session:
        bitcoin, euro, gold = await asyncio.gather(
            *(fetch(session, url) for url in urls)
        )

    print(f"Bitcoin: {bitcoin['bitcoin']['usd']} USD")
    print(f"EUR/USD: {euro['rate']}")
    print(f"Złoto: {gold['spot_usd_oz']} USD/oz")


if __name__ == "__main__":
    asyncio.run(main())