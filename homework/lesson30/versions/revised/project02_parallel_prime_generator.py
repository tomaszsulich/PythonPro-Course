from concurrent.futures import ProcessPoolExecutor
import math
import time
import multiprocessing


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def process_range(bounds: tuple[int, int]) -> list[int]:
    start, end = bounds

    return [
        number
        for number in range(start, end)
        if is_prime(number)
    ]


def main() -> None:
    start_num = 1_000_000
    end_num = 1_300_000
    cpus = multiprocessing.cpu_count()
    chunk_size = (end_num - start_num) // cpus

    bounds = []

    for i in range(cpus):
        start = start_num + i * chunk_size

        end = (
            end_num
            if i == cpus - 1
            else start + chunk_size
        )

        bounds.append((start, end))

    start_sequential = time.perf_counter()

    sequential_result = process_range(
        (start_num, end_num)
    )

    sequential_time = time.perf_counter() - start_sequential

    start_parallel = time.perf_counter()

    with ProcessPoolExecutor(max_workers=cpus) as executor:
        partial_results = executor.map(process_range, bounds)

        parallel_result = [
            number
            for result in partial_results
            for number in result
        ]

    parallel_time = time.perf_counter() - start_parallel

    print(f"Liczba rdzeni CPU: {cpus}")
    print(f"Liczba znalezionych liczb pierwszych: {len(parallel_result)}")
    print(f"Czas sekwencyjny: {sequential_time} s")
    print(f"Czas równoległy: {parallel_time} s")
    print(f"Wyniki zgodne: {sequential_result == parallel_result}")


if __name__ == "__main__":
    main()