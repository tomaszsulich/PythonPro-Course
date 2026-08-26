import multiprocessing
import random


NUMBER_COUNT = 100
MIN_NUMBER = 1
MAX_NUMBER = 1000


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def main() -> None:
    numbers = [
        random.randint(MIN_NUMBER, MAX_NUMBER)
        for _ in range(NUMBER_COUNT)
    ]

    with multiprocessing.Pool() as pool:
        results = pool.map(is_prime, numbers)

    prime_count = sum(results)

    print(f"Wylosowane liczby: {numbers}\n")
    print(f"Wyniki sprawdzania: {results}\n")
    print(f"Liczba znalezionych liczb pierwszych: {prime_count}")


if __name__ == "__main__":
    main()