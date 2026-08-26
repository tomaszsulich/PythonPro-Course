import asyncio


async def producer(queue: asyncio.Queue[int | None]) -> None:
    for number in range(1, 21):
        await asyncio.sleep(0.5)
        await queue.put(number)


async def consumer(consumer_id: int, queue: asyncio.Queue[int | None]) -> None:
    while True:
        number = await queue.get()

        if number is None:
            queue.task_done()
            break

        print(f"Konsument {consumer_id} przetworzył liczbę: {number}")
        queue.task_done()


async def main() -> None:
    queue = asyncio.Queue()

    consumers = [
        asyncio.create_task(consumer(consumer_id, queue))
        for consumer_id in range(1, 3)
    ]

    await producer(queue)
    await queue.join()

    for _ in consumers:
        await queue.put(None)

    await asyncio.gather(*consumers)


if __name__ == "__main__":
    asyncio.run(main())