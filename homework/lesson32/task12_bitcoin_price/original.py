import aiohttp
import asyncio


async def main() -> None:
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

    bitcoin_price = data["bpi"]["USD"]["rate"]

    print(f"Cena Bitcoina: {bitcoin_price} USD")


if __name__ == "__main__":
    asyncio.run(main())