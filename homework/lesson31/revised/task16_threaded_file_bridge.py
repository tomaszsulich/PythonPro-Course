import asyncio
from pathlib import Path


FILE_COUNT = 100
DATA_DIR = Path("task16_files")


def read_file(file_path: Path) -> bytes:
    return file_path.read_bytes()


async def main() -> None:
    file_paths = sorted(
        file_path
        for file_path in DATA_DIR.iterdir()
        if file_path.is_file()
    )

    if len(file_paths) != FILE_COUNT:
        print(
            f"Oczekiwano {FILE_COUNT} plików, "
            f"znaleziono: {len(file_paths)}."
        )
        return

    contents = await asyncio.gather(
        *(
            asyncio.to_thread(read_file, file_path)
            for file_path in file_paths
        )
    )

    non_empty_files = sum(bool(content) for content in contents)
    total_bytes = sum(len(content) for content in contents)

    print(f"Odczytano plików: {len(contents)}")
    print(f"Niepustych plików: {non_empty_files}")
    print(f"Łączny rozmiar: {total_bytes} B")


if __name__ == "__main__":
    asyncio.run(main())