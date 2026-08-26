import threading


numbers = []
lock = threading.Lock()


def add_numbers(number: int) -> None:
    for _ in range(100_000):
        with lock:
            numbers.append(number)


def main() -> None:
    thread_1 = threading.Thread(
        target=add_numbers,
        args=(1,),
    )

    thread_2 = threading.Thread(
        target=add_numbers,
        args=(2,),
    )

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    list_length = len(numbers)

    print(f"Długość listy: {list_length}")
    print(f"Oczekiwana długość: {200_000}")
    print(f"Poprawny wynik: {list_length == 200_000}")


if __name__ == "__main__":
    main()