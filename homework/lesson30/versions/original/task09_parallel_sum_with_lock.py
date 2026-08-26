import threading
from itertools import islice


# Polskie nazewnictwo sumowania zachowano dla spójności z wymaganą zmienną suma_calkowita.
suma_calkowita: float | int = 0
lock = threading.Lock()


def sumuj_czesc(liczby: list[float | int], start: int, end: int) -> None:
    global suma_calkowita

    suma_czesciowa = sum(islice(liczby, start, end))

    with lock:
        suma_calkowita += suma_czesciowa


def main() -> None:
    liczby = list(range(1, 10_000_001))
    thread_count = 4
    chunk_size = len(liczby) // thread_count
    threads = []

    for thread_number in range(thread_count):
        start = thread_number * chunk_size

        end = (
            len(liczby)
            if thread_number == thread_count - 1
            else start + chunk_size
        )

        thread = threading.Thread(
            target=sumuj_czesc,
            args=(liczby, start, end),
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    suma_oczekiwana = sum(liczby)

    print(f"Suma całkowita: {suma_calkowita}")
    print(f"Oczekiwana suma: {suma_oczekiwana}")
    print(f"Poprawny wynik: {suma_calkowita == suma_oczekiwana}")


if __name__ == "__main__":
    main()