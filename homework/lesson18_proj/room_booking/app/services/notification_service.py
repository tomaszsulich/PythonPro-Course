from datetime import datetime, timedelta, timezone

from ..db import db
from ..models import Booking, Notification


def create_upcoming_reminders():
    """Tworzy przypomnienia dla rezerwacji zaczynających się za około godzinę."""
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    window_start = now + timedelta(minutes=55)
    window_end = now + timedelta(minutes=65)

    bookings = Booking.query.filter(
        Booking.status != "cancelled",
        Booking.start_time >= window_start,
        Booking.start_time <= window_end,
    ).all()

    for booking in bookings:
        message = f"Przypomnienie: rezerwacja '{booking.title}' zaczyna się za 1h"
        exists = Notification.query.filter_by(
            user_id=booking.user_id, message=message
        ).first()
        if not exists:
            db.session.add(Notification(user_id=booking.user_id, message=message))

    db.session.commit()


def get_unread_notifications():
    create_upcoming_reminders()
    return Notification.query.filter_by(is_read=False).order_by(
        Notification.created_at.desc()
    ).all()


def mark_as_read(notification_id):
    notification = db.session.get(Notification, notification_id)
    if not notification:
        raise ValueError("Powiadomienie nie istnieje.")
    notification.is_read = True
    db.session.commit()
    return notification
