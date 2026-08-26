import asyncio
import random


# Nazwa funkcji i parametru zgodna z treścią zadania.
async def ping(host: str) -> str:
    await asyncio.sleep(random.uniform(0.1, 1.0))
    return f"Host {host} odpowiada"


async def main() -> None:
    hosts = [
        "server1.example.com",
        "server2.example.com",
        "server3.example.com",
        "server4.example.com",
        "server5.example.com",
    ]

    results = await asyncio.gather(
        *(ping(host) for host in hosts)
    )

    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())