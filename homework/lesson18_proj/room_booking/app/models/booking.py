from .base import db, Base
from datetime import datetime, timezone
from sqlalchemy import event, select


class Booking(Base):
    """Model rezerwacji sali."""
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)

    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    status = db.Column(db.String(20), default='confirmed',
                       nullable=False)  # confirmed, cancelled, completed

    attendees_count = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime,
                           default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime,
                           default=lambda: datetime.now(timezone.utc),
                           onupdate=lambda: datetime.now(timezone.utc))
    applied_hourly_rate = db.Column(db.Numeric(10, 2),
                                    default=0,
                                    nullable=False)
    recurrence_rule = db.Column(db.String(20))
    series_id = db.Column(db.String(36), index=True)

    # Indeks dla szybkiego wyszukiwania
    __table_args__ = (db.Index('idx_booking_room_time', 'room_id',
                               'start_time', 'end_time'), )

    def __repr__(self):
        return f'<Booking {self.title} ({self.start_time})>'

    @property
    def duration_hours(self):
        """Czas trwania rezerwacji w godzinach."""
        delta = self.end_time - self.start_time
        return delta.total_seconds() / 3600

    @property
    def total_cost(self):
        """Całkowity koszt rezerwacji na podstawie stawki historycznej."""
        return float(self.applied_hourly_rate) * self.duration_hours

    def to_dict(self, include_room=False, include_user=False):
        data = super().to_dict()
        if include_room:
            data['room'] = self.room.to_dict(include_equipment=False)
        if include_user:
            data['user'] = self.user.to_dict()
        return data


@event.listens_for(Booking, "after_insert")
def notify_admins_after_booking_insert(mapper, connection, target):
    """Tworzy minimalne powiadomienie dla każdego administratora."""
    from .notification import Notification
    from .user import User

    admin_ids = connection.execute(
        select(User.id).where(User.is_admin.is_(True))
    ).scalars()

    for admin_id in admin_ids:
        connection.execute(
            Notification.__table__.insert().values(
                user_id=admin_id,
                message=f"Nowa rezerwacja: {target.title}",
                is_read=False,
                created_at=datetime.now(timezone.utc),
            )
        )
