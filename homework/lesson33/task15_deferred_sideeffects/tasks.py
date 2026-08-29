from pathlib import Path


EMAIL_LOG = Path("emails.log")
STATISTICS_LOG = Path("statistics.log")


def send_book_email(book_id: int, title: str) -> None:
    with EMAIL_LOG.open("a", encoding="utf-8") as file:
        file.write(
            "Wysłano e-mail po utworzeniu książki "
            f"{book_id}: {title}\n"
        )


def update_statistics() -> None:
    deleted_books = 0

    if STATISTICS_LOG.exists():
        content = STATISTICS_LOG.read_text(encoding="utf-8").strip()

        if content:
            deleted_books = int(content.split(": ")[1])

    deleted_books += 1

    STATISTICS_LOG.write_text(
        f"Usunięte książki: {deleted_books}",
        encoding="utf-8"
    )