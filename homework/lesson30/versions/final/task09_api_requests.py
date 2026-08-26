import random
import time
from concurrent.futures import ThreadPoolExecutor


REQUEST_COUNT = 20
WORKER_COUNT = 5


def simulate_api_request(request_id: int) -> int:
    time.sleep(random.uniform(0.5, 2.0))
    return request_id


def main() -> None:
    request_ids = list(range(1, REQUEST_COUNT + 1))

    start = time.perf_counter()

    for request_id in request_ids:
        simulate_api_request(request_id)

    sequential_time = time.perf_counter() - start

    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=WORKER_COUNT) as executor:
        list(executor.map(simulate_api_request, request_ids))

    threaded_time = time.perf_counter() - start
    speedup = sequential_time / threaded_time

    print(f"Sekwencyjnie: {sequential_time:.2f} s")
    print(f"Równolegle: {threaded_time:.2f} s")
    print(f"Przyspieszenie: {speedup:.2f}×")


if __name__ == "__main__":
    main()