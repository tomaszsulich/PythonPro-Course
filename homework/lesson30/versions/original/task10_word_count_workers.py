import re
import threading
from pathlib import Path


total_count = 0
lock = threading.Lock()


def count_word(file_path: Path, word: str) -> None:
    global total_count

    content = file_path.read_text(encoding="utf-8")

    pattern = re.compile(
        rf"(?<!\w){re.escape(word)}(?!\w)",
        re.IGNORECASE,
    )

    file_count = len(pattern.findall(content))

    with lock:
        total_count += file_count


def main() -> None:
    word = input("Podaj szukane słowo: ")
    text_files = list(Path.cwd().glob("*.txt"))
    threads = []

    for file_path in text_files:
        thread = threading.Thread(
            target=count_word,
            args=(file_path, word),
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Łączna liczba wystąpień słowa '{word}': {total_count}")


if __name__ == "__main__":
    main()