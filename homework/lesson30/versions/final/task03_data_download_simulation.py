import threading
import time


# Polskie nazewnictwo zachowano zgodnie z treścią zadania.
def pobierz_dane(id_danych: int) -> None:
    print(f"Pobieram dane {id_danych}...")
    time.sleep(2)
    print(f"Pobrano dane {id_danych}.")


def main() -> None:
    data_ids = [1, 2, 3]

    start = time.perf_counter()

    for data_id in data_ids:
        pobierz_dane(data_id)

    sequential_time = time.perf_counter() - start
    start = time.perf_counter()
    threads = []

    for data_id in data_ids:
        thread = threading.Thread(
            target=pobierz_dane,
            args=(data_id,),
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    threaded_time = time.perf_counter() - start
    speedup = sequential_time / threaded_time

    print(f"Sekwencyjnie: {sequential_time:.2f} s")
    print(f"Wielowątkowo: {threaded_time:.2f} s")
    print(f"Przyspieszenie: {speedup:.2f}×")


if __name__ == "__main__":
    main()