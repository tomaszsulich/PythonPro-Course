import random
import time
from concurrent.futures import ThreadPoolExecutor


# Polskie nazewnictwo zachowano zgodnie z treścią zadania.
LICZBA_WATKOW = 5

OPINIE = [
    "Produkt działa dokładnie tak, jak oczekiwałem.",
    "Jakość wykonania jest bardzo dobra.",
    "Przesyłka dotarła znacznie później niż powinna.",
    "Obsługa klienta szybko rozwiązała mój problem.",
    "Produkt przestał działać po kilku dniach.",
    "Cena jest adekwatna do jakości.",
    "Opakowanie było uszkodzone.",
    "Produkt jest łatwy w obsłudze.",
    "Nie zauważyłem żadnej szczególnej różnicy.",
    "Jestem bardzo zadowolony z zakupu.",
    "Instrukcja mogłaby być bardziej czytelna.",
    "Produkt spełnia podstawowe wymagania.",
    "Kolor wygląda inaczej niż na zdjęciach.",
    "Dostawa przebiegła szybko i bez problemów.",
    "Nie kupiłbym tego produktu ponownie.",
    "Wszystko działa poprawnie.",
    "Produkt jest przeciętny, ale spełnia swoje zadanie.",
    "Materiały wydają się solidne.",
    "Cena jest zdecydowanie za wysoka.",
    "Zakup okazał się dobrym wyborem.",
]


def analizuj_sentyment(zdanie: str) -> tuple[str, str]:
    time.sleep(random.uniform(0.5, 2.0))

    sentyment = random.choice(
        ["Pozytywny", "Negatywny", "Neutralny"],
    )

    return zdanie, sentyment


def main() -> None:
    czas_startu = time.perf_counter()

    with ThreadPoolExecutor(max_workers=LICZBA_WATKOW) as wykonawca:
        wyniki = list(wykonawca.map(analizuj_sentyment, OPINIE))

    czas_wykonania = time.perf_counter() - czas_startu

    for opinia, sentyment in wyniki:
        print(f"{sentyment}: {opinia}")

    print(f"\nCzas wykonania: {czas_wykonania:.2f} s")


if __name__ == "__main__":
    main()