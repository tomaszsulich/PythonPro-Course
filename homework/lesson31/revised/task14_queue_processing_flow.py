import asyncio


async def producer(queue: asyncio.Queue[int | None]) -> None:
    for number in range(1, 21):
        await asyncio.sleep(0.5)
        await queue.put(number)

    await queue.put(None)


async def consumer(queue: asyncio.Queue[int | None]) -> None:
    while True:
        number = await queue.get()

        if number is None:
            queue.task_done()
            break

        print(f"Przetworzono liczbę: {number}")
        queue.task_done()


async def main() -> None:
    queue: asyncio.Queue[int | None] = asyncio.Queue()

    await asyncio.gather(
        producer(queue),
        consumer(queue),
    )

    await queue.join()


if __name__ == "__main__":
    asyncio.run(main())