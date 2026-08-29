from pathlib import Path


EMAIL_LOG = Path("comment_emails.log")


def send_comment_email(email: str, post_title: str) -> None:
    with EMAIL_LOG.open("a", encoding="utf-8") as file:
        file.write(
            f"Wysłano e-mail do {email}: "
            f"nowy komentarz do posta '{post_title}'.\n"
        )