import multiprocessing
import threading
import time


WORK_SIZE = 20_000_000
RUN_COUNT = 2


def cpu_bound_work(size: int) -> int:
    return sum(number * number for number in range(size))


def measure_sequential() -> float:
    start = time.perf_counter()

    for _ in range(RUN_COUNT):
        cpu_bound_work(WORK_SIZE)

    return time.perf_counter() - start


def measure_threads() -> float:
    threads = [
        threading.Thread(
            target=cpu_bound_work,
            args=(WORK_SIZE,),
        )
        for _ in range(RUN_COUNT)
    ]

    start = time.perf_counter()

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return time.perf_counter() - start


def measure_processes() -> float:
    processes = [
        multiprocessing.Process(
            target=cpu_bound_work,
            args=(WORK_SIZE,),
        )
        for _ in range(RUN_COUNT)
    ]

    start = time.perf_counter()

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    return time.perf_counter() - start


# W standardowym CPythonie z GIL dwa wątki nie wykonują jednocześnie
# kodu bajtowego Pythona, dlatego przy zadaniu CPU-bound nie powinny
# zapewnić istotnego przyspieszenia względem wykonania sekwencyjnego.
# Osobne procesy mają własne interpretery i mogą wykorzystać różne
# rdzenie procesora, choć ich uruchamianie wiąże się z dodatkowym narzutem.
def main() -> None:
    sequential_time = measure_sequential()
    threaded_time = measure_threads()
    process_time = measure_processes()

    thread_speedup = sequential_time / threaded_time
    process_speedup = sequential_time / process_time

    print(f"Sekwencyjnie: {sequential_time:.2f} s")
    print(f"Dwa wątki: {threaded_time:.2f} s")
    print(f"Dwa procesy: {process_time:.2f} s")
    print(f"Przyspieszenie wątków: {thread_speedup:.2f}×")
    print(f"Przyspieszenie procesów: {process_speedup:.2f}×")


if __name__ == "__main__":
    main()