import multiprocessing


def get_name(queue: multiprocessing.Queue) -> None:
    name = input("Podaj imię: ")
    queue.put(name)


def main() -> None:
    queue = multiprocessing.Queue()

    process = multiprocessing.Process(
        target=get_name,
        args=(queue,),
    )

    process.start()
    name = queue.get()
    process.join()
    print(f"Witaj, {name}!")


if __name__ == "__main__":
    main()