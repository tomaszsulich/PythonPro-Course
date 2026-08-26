import multiprocessing


# Nazwa funkcji i parametrów zgodna z treścią zadania.
def potega(liczba: int, pot: int) -> None:
    result = liczba ** pot
    print(f"{liczba}^{pot} = {result}")


def main() -> None:
    process = multiprocessing.Process(
        target=potega,
        args=(5, 3),
    )
    process.start()
    process.join()


if __name__ == "__main__":
    main()