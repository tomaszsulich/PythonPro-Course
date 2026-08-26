import queue
import random
import threading
import time


def producer(shared_queue: queue.Queue[int], stop_event: threading.Event) -> None:
    """Dodaje losowe liczby do kolejki do momentu zatrzymania."""
    while not stop_event.is_set():
        number = random.randint(1, 100)

        print(f"Producent przygotował: {number}")
        shared_queue.put(number)

        stop_event.wait(1)


def consumer(shared_queue: queue.Queue[int], stop_event: threading.Event) -> None:
    """Pobiera i przetwarza elementy kolejki do momentu zatrzymania."""
    while not stop_event.is_set():
        try:
            number = shared_queue.get(timeout=0.1)
        except queue.Empty:
            continue

        print(f"Konsument pobrał: {number}")
        shared_queue.task_done()
        stop_event.wait(1.5)


def main() -> None:
    shared_queue = queue.Queue()
    stop_event = threading.Event()

    producer_thread = threading.Thread(
        target=producer,
        args=(shared_queue, stop_event),
    )

    consumer_thread = threading.Thread(
        target=consumer,
        args=(shared_queue, stop_event),
    )

    producer_thread.start()
    consumer_thread.start()

    time.sleep(10)
    stop_event.set()

    producer_thread.join()
    consumer_thread.join()

    print("Program zakończył pracę.")


if __name__ == "__main__":
    main()