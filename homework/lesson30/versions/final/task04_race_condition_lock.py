import threading


shared_list = []
lock = threading.Lock()


def add_elements_without_lock(value: int) -> None:
    for _ in range(100_000):
        shared_list.append(value)


def add_elements_with_lock(value: int) -> None:
    for _ in range(100_000):
        with lock:
            shared_list.append(value)


def run_without_lock() -> int:
    global shared_list
    shared_list = []

    threads = [
        threading.Thread(
            target=add_elements_without_lock,
            args=(value,),
        )
        for value in (1, 2)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return len(shared_list)


def run_with_lock() -> int:
    global shared_list
    shared_list = []

    threads = [
        threading.Thread(
            target=add_elements_with_lock,
            args=(value,),
        )
        for value in (1, 2)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return len(shared_list)


def main() -> None:
    print("Bez Lock:")

    for attempt in range(1, 4):
        result = run_without_lock()
        print(f"Próba {attempt}: {result}")

    print("\nZ Lock:")

    for attempt in range(1, 4):
        result = run_with_lock()
        print(f"Próba {attempt}: {result}")


if __name__ == "__main__":
    main()