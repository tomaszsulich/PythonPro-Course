import hashlib
import multiprocessing
from pathlib import Path


SOURCE_DIRECTORY = Path("task16_files")
CHUNK_SIZE = 8192


def calculate_sha256(file_path: Path) -> tuple[str, str]:
    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:
        while chunk := file.read(CHUNK_SIZE):
            sha256.update(chunk)

    return file_path.name, sha256.hexdigest()


def main() -> None:
    files = sorted(
        path
        for path in SOURCE_DIRECTORY.iterdir()
        if path.is_file()
    )

    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_sha256, files)

    hashes = dict(results)

    print("{")

    for index, (file_name, file_hash) in enumerate(hashes.items()):
        comma = "," if index < len(hashes) - 1 else ""
        print(f"    {file_name!r}: {file_hash!r}{comma}")

    print("}")
    print()


if __name__ == "__main__":
    main()