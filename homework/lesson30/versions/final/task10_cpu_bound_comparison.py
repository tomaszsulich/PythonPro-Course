import multiprocessing
import random
import time
from concurrent.futures import ThreadPoolExecutor


NUMBER_COUNT = 100
MIN_NUMBER = 1
MAX_NUMBER = 1000
WORK_SIZE = 20_000_000


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def cpu_bound_work(size: int) -> int:
    return sum(number * number for number in range(size))


def main() -> None:
    numbers = [
        random.randint(MIN_NUMBER, MAX_NUMBER)
        for _ in range(NUMBER_COUNT)
    ]

    with multiprocessing.Pool() as pool:
        prime_results = pool.map(is_prime, numbers)

    prime_count = sum(prime_results)

    work_sizes = [WORK_SIZE, WORK_SIZE]

    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=2) as executor:
        list(executor.map(cpu_bound_work, work_sizes))

    threaded_time = time.perf_counter() - start

    start = time.perf_counter()

    with multiprocessing.Pool(processes=2) as pool:
        pool.map(cpu_bound_work, work_sizes)

    process_time = time.perf_counter() - start

    speedup = threaded_time / process_time

    print(f"Liczba znalezionych liczb pierwszych: {prime_count}")
    print(f"Wątki: {threaded_time:.2f} s")
    print(f"Procesy: {process_time:.2f} s")
    print(f"Przyspieszenie względem wątków: {speedup:.2f}×")


if __name__ == "__main__":
    main()