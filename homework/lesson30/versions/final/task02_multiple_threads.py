import threading


def worker(thread_number: int) -> None:
    print(f"Jestem wątkiem numer {thread_number}.")


def main() -> None:
    threads = []

    for thread_number in range(1, 6):
        thread = threading.Thread(
            target=worker,
            args=(thread_number,),
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()