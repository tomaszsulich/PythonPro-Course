import aiohttp
import asyncio


async def fetch(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def main() -> None:
    urls = [
        "https://api.publicapis.org/random?auth=null",
        "https://api.publicapis.org/random?auth=null",
        "https://api.publicapis.org/random?auth=null",
    ]

    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *(fetch(session, url) for url in urls)
        )

    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())