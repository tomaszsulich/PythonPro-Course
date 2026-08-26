import argparse
import multiprocessing
import random
import time


# Polskie nazewnictwo zachowano zgodnie z treścią zadania.
LICZBA_OBRAZOW = 10
SZEROKOSC_OBRAZU = 1000
WYSOKOSC_OBRAZU = 1000


def zastosuj_filtr(obraz: list[list[int]], liczba_operacji: int) -> list[list[float]]:
    wynik = []

    for wiersz in obraz:
        nowy_wiersz = []

        for piksel in wiersz:
            wartosc = piksel

            for _ in range(liczba_operacji):
                wartosc *= 1.1

            nowy_wiersz.append(wartosc)
        wynik.append(nowy_wiersz)
    return wynik


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--liczba-operacji",
        type=int,
        default=1,
    )

    args = parser.parse_args()

    obrazy = [
        [
            [random.randint(0, 255) for _ in range(SZEROKOSC_OBRAZU)]
            for _ in range(WYSOKOSC_OBRAZU)
        ]
        for _ in range(LICZBA_OBRAZOW)
    ]

    start_sekwencyjny = time.perf_counter()

    wyniki_sekwencyjne = [
        zastosuj_filtr(obraz, args.liczba_operacji)
        for obraz in obrazy
    ]

    czas_sekwencyjny = time.perf_counter() - start_sekwencyjny

    del wyniki_sekwencyjne

    start_rownolegly = time.perf_counter()

    argumenty = [
        (obraz, args.liczba_operacji)
        for obraz in obrazy
    ]

    with multiprocessing.Pool() as pula:
        wyniki_rownolegle = pula.starmap(zastosuj_filtr, argumenty)

    czas_rownolegly = time.perf_counter() - start_rownolegly

    del wyniki_rownolegle

    przyspieszenie = czas_sekwencyjny / czas_rownolegly

    print(f"Sekwencyjnie: {czas_sekwencyjny} s")
    print(f"Równolegle: {czas_rownolegly} s")
    print(f"Przyspieszenie: {przyspieszenie}×")


if __name__ == "__main__":
    main()