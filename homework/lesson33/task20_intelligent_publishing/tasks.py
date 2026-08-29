from pathlib import Path

from sqlalchemy import select

from ai_service import analyze_sentiment
from database import AsyncSessionLocal
from models import Comment


EMAIL_LOG = Path("comment_emails.log")


def send_comment_email(email: str, post_title: str) -> None:
    with EMAIL_LOG.open("a", encoding="utf-8") as file:
        file.write(
            f"Wysłano e-mail do {email}: "
            f"nowy komentarz do posta '{post_title}'.\n"
        )


async def analyze_comment_sentiment(comment_id: int) -> None:
    async with AsyncSessionLocal() as db:
        result = await db.execute(
            select(Comment).where(Comment.id == comment_id)
        )
        comment = result.scalar_one_or_none()

        if comment is None:
            return

        comment.sentiment = await analyze_sentiment(comment.content)
        await db.commit()