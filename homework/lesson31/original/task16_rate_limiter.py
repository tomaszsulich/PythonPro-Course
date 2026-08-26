import asyncio
import time
from collections import deque


RATE_LIMIT = 5
TASK_COUNT = 20
REQUESTS_PER_TASK = 2


class RateLimiter:
    def __init__(self, rate: int) -> None:
        self.rate = rate
        self.timestamps: deque[float] = deque()
        self.lock = asyncio.Lock()

    async def acquire(self) -> None:
        while True:
            async with self.lock:
                now = time.monotonic()

                while (
                    self.timestamps
                    and now - self.timestamps[0] >= 1
                ):
                    self.timestamps.popleft()

                if len(self.timestamps) < self.rate:
                    self.timestamps.append(now)
                    return

                wait_time = 1 - (now - self.timestamps[0])

            await asyncio.sleep(wait_time)


async def worker(task_id: int, limiter: RateLimiter) -> None:
    for request_number in range(1, REQUESTS_PER_TASK + 1):
        await limiter.acquire()

        print(
            f"Zadanie {task_id:02d}, "
            f"próba {request_number}: uzyskano dostęp."
        )


async def main() -> None:
    limiter = RateLimiter(RATE_LIMIT)

    print(
        f"Uruchamiam {TASK_COUNT} zadań, każde wykona "
        f"{REQUESTS_PER_TASK} próby."
    )

    print(
        f"Limit wynosi {RATE_LIMIT} zapytań na sekundę, "
        "więc kolejne zadania mogą chwilę czekać.\n"
    )

    start = time.perf_counter()

    await asyncio.gather(
        *(
            worker(task_id, limiter)
            for task_id in range(1, TASK_COUNT + 1)
        )
    )

    execution_time = time.perf_counter() - start
    request_count = TASK_COUNT * REQUESTS_PER_TASK
    minimum_time = (request_count // RATE_LIMIT) - 1

    print(f"\nWykonano łącznie: {request_count} prób.")
    print(f"Czas wykonania: {execution_time:.2f} s")
    print(f"Oczekiwany minimalny czas: około {minimum_time} s")

    if execution_time >= minimum_time:
        print("TEST OK: ogranicznik zachował wymagany limit.")
    else:
        print("TEST FAILED: zadania wykonano zbyt szybko.")


if __name__ == "__main__":
    asyncio.run(main())