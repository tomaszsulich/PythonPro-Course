import shutil
import threading
from pathlib import Path


def copy_file(source_file: Path, target_directory: Path) -> None:
    """Kopiuje pojedynczy plik do katalogu docelowego."""
    print(f"Kopiowanie pliku {source_file.name}...")

    target_file = target_directory / source_file.name
    shutil.copy2(source_file, target_file)

    print(f"Ukończono kopiowanie pliku {source_file.name}.")


def main() -> None:
    source_directory = Path("task14_source")
    target_directory = Path("task14_target")

    target_directory.mkdir(exist_ok=True)

    files = [
        path
        for path in source_directory.iterdir()
        if path.is_file()
    ]

    threads = []

    for source_file in files:
        thread = threading.Thread(
            target=copy_file,
            args=(source_file, target_directory),
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Wszystkie pliki zostały skopiowane.")


if __name__ == "__main__":
    main()