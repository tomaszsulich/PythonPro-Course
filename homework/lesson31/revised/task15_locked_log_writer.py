import asyncio
import aiofiles


LOG_FILE = "task15_logs.txt"
COROUTINE_COUNT = 5


async def write_log(coroutine_id: int, lock: asyncio.Lock) -> None:
    log_entry = f"Log z korutyny {coroutine_id}\n"

    async with lock:
        async with aiofiles.open(
            LOG_FILE,
            "a",
            encoding="utf-8",
        ) as file:
            await file.write(log_entry)


async def main() -> None:
    lock = asyncio.Lock()

    await asyncio.gather(
        *(
            write_log(coroutine_id, lock)
            for coroutine_id in range(1, COROUTINE_COUNT + 1)
        )
    )

    print(f"Zapisano {COROUTINE_COUNT} logów do pliku {LOG_FILE}.")


if __name__ == "__main__":
    asyncio.run(main())