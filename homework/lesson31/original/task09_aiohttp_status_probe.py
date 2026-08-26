import asyncio
import aiohttp


URLS = [
    "https://example.com",
    "https://www.python.org",
    "https://httpbin.org/status/200",
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/500",
]


async def check_status(session: aiohttp.ClientSession,url: str) -> tuple[str, int | None]:
    try:
        async with session.get(url) as response:
            return url, response.status
    except aiohttp.ClientError:
        return url, None


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *(check_status(session, url) for url in URLS)
        )

    for url, status in results:
        if status is None:
            print(f"{url} - Błąd połączenia")
        else:
            print(f"{url} - Status: {status}")


if __name__ == "__main__":
    asyncio.run(main())