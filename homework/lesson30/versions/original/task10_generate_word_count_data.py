import random
from pathlib import Path


TARGET_WORD = "Python"

FILE_COUNTS = {
    "task10_data_1.txt": 10_000,
    "task10_data_2.txt": 25_000,
    "task10_data_3.txt": 40_000,
}

SENTENCES = [
    "Coraz więcej procesów biznesowych wykorzystuje automatyzację.",
    "Analiza dużych zbiorów danych wymaga odpowiednio dobranych narzędzi.",
    "Czytelny kod ułatwia rozwijanie i utrzymywanie aplikacji.",
    "Testy automatyczne pomagają szybko wykrywać regresje.",
    "Przetwarzanie plików jest częstym elementem aplikacji użytkowych.",
    "Współbieżność może przyspieszyć operacje zależne od wejścia i wyjścia.",
    "Dobrze zaprojektowany program powinien być łatwy do rozszerzania.",
    "Automatyzacja ogranicza liczbę powtarzalnych czynności wykonywanych ręcznie.",
]

WORD_CONTEXTS = [
    "Python dobrze sprawdza się w automatyzacji zadań.",
    "Do analizy danych wykorzystano język Python.",
    "W tym przykładzie Python służy do pracy z tekstem.",
    "Do wykonania zadania wybrano PYTHON jako język programowania.",
    "Kolejny moduł aplikacji również wykorzystuje python."
]


def build_file(file_path: Path, word_count: int) -> None:
    with file_path.open("w", encoding="utf-8") as file:
        for _ in range(word_count):
            file.write(f"{random.choice(SENTENCES)} ")
            file.write(f"{random.choice(WORD_CONTEXTS)} ")
            file.write(f"{random.choice(SENTENCES)}\n")


def main() -> None:
    for filename, word_count in FILE_COUNTS.items():
        build_file(Path(filename), word_count)

    expected_total = sum(FILE_COUNTS.values())

    print(f"Utworzono {len(FILE_COUNTS)} pliki.")
    print(f"Oczekiwana liczba wystąpień '{TARGET_WORD}': {expected_total}")


if __name__ == "__main__":
    main()