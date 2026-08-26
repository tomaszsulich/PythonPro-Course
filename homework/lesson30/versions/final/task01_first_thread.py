import threading
import time


def worker() -> None:
    time.sleep(3)
    print("Wątek zakończył pracę!")


def main() -> None:
    thread = threading.Thread(target=worker)
    thread.start()

    print("Główny program czeka na wątek...")

    thread.join()


if __name__ == "__main__":
    main()