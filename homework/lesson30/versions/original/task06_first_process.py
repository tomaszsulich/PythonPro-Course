import multiprocessing


def calculate_factorial(number: int) -> None:
    result = 1

    for value in range(2, number + 1):
        result *= value

    print(f"{number}! = {result}")


def main() -> None:
    process = multiprocessing.Process(
        target=calculate_factorial,
        args=(10,),
    )
    process.start()
    process.join()


if __name__ == "__main__":
    main()