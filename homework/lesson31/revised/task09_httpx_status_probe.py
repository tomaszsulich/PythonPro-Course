import asyncio
import httpx


URLS = [
    "https://www.google.com",
    "https://www.python.org",
    "https://www.github.com",
]


async def fetch_status(client: httpx.AsyncClient, url: str) -> tuple[str, int]:
    response = await client.get(url)
    return url, response.status_code


async def main() -> None:
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(
            *(fetch_status(client, url) for url in URLS)
        )

    for url, status_code in results:
        print(f"{url} - Status: {status_code}")


if __name__ == "__main__":
    asyncio.run(main())