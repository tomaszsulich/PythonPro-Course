import asyncio

async def main(n):
    for _ in range(n, 0, -1):
        await asyncio.sleep(1)
    print("odczekane")
    
asyncio.run(main(3))