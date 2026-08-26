import multiprocessing


def _parsuj_liczbe(wartosc: str) -> int | float:
    liczba = float(wartosc)
    return int(liczba) if liczba.is_integer() else liczba


def oblicz_statystyki(polaczenie: multiprocessing.connection.Connection) -> None:
    liczby = polaczenie.recv()

    suma = sum(liczby)
    srednia = suma / len(liczby)

    polaczenie.send((suma, srednia))
    polaczenie.close()


def main() -> None:
    liczby = [
        _parsuj_liczbe(wartosc)
        for wartosc in input(
            "Podaj co najmniej 2 liczby oddzielone spacjami: "
        ).split()
    ]

    if len(liczby) < 2:
        print("Podaj co najmniej 2 liczby.")
        return

    polaczenie_nadrzedne, polaczenie_potomne = multiprocessing.Pipe()

    proces = multiprocessing.Process(
        target=oblicz_statystyki,
        args=(polaczenie_potomne,),
    )
    proces.start()

    polaczenie_nadrzedne.send(liczby)
    suma, srednia = polaczenie_nadrzedne.recv()

    proces.join()
    polaczenie_nadrzedne.close()

    print(f"Suma: {suma}")
    print(f"Średnia: {srednia:.2f}")


if __name__ == "__main__":
    main()