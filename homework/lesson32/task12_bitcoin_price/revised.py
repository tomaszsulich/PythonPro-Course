import aiohttp
import asyncio


async def main() -> None:
    # Endpoint CoinDesk z zadania jest już niedostępny,
    # dlatego używamy publicznego API CoinGecko.
    url = (
        "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    )
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
    
    bitcoin_price = data["bitcoin"]["usd"]
    
    print(f"Cena Bitcoina: {bitcoin_price} USD")


if __name__ == "__main__":
    asyncio.run(main())