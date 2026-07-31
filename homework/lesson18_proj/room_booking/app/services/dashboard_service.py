from datetime import datetime, timedelta, timezone
from sqlalchemy import func, desc, extract
from ..db import db
from ..models import Room, Booking, User


def get_booking_statistics(start_date=None, end_date=None):
    """Wyodrębniona logika statystyk, sprowadzona bezpośrednio do warstwy serwisowej."""
    base_query = Booking.query.filter(Booking.status != 'cancelled')

    if start_date:
        base_query = base_query.filter(Booking.start_time >= start_date)
    if end_date:
        base_query = base_query.filter(Booking.end_time <= end_date)

    total_bookings = base_query.count()

    room_stats = db.session.query(
        Room.name,
        func.count(Booking.id).label('booking_count'),
        func.sum(
            (func.julianday(Booking.end_time) -
             func.julianday(Booking.start_time)) * 24).label('total_hours')).join(Booking).filter(
                Booking.status != 'cancelled').group_by(Room.name).all()

    weekday_stats = db.session.query(
        extract('dow', Booking.start_time).label('weekday'),
        func.count(Booking.id).label('count')).filter(
            Booking.status != 'cancelled').group_by('weekday').order_by(
                'weekday').all()

    weekdays = ['Nd', 'Pn', 'Wt', 'Śr', 'Cz', 'Pt', 'Sb']

    return {
        'total_bookings':
        total_bookings,
        'room_stats': [{
            'room': r.name,
            'bookings': r.booking_count,
            'hours': round(float(r.total_hours or 0), 1)
        } for r in room_stats],
        'weekday_stats': [{
            'day': weekdays[int(w.weekday)],
            'count': w.count
        } for w in weekday_stats]
    }


def get_dashboard_summary():
    now = datetime.now(timezone.utc)
    today_date = now.date()
    month_ago = now - timedelta(days=30)

    stats = {
        'total_rooms':
        Room.query.filter_by(is_active=True).count(),
        'total_users':
        User.query.count(),
        'total_bookings':
        Booking.query.filter_by(status='confirmed').count(),
        'bookings_today':
        Booking.query.filter(
            func.date(Booking.start_time) == today_date,
            Booking.status == 'confirmed').count()
    }

    upcoming = Booking.query.options(db.joinedload(
        Booking.room), db.joinedload(Booking.user)).filter(
            Booking.start_time >= now, Booking.start_time
            <= now + timedelta(hours=24),
            Booking.status == 'confirmed').order_by(
                Booking.start_time).limit(10).all()

    top_users = db.session.query(
        User.name,
        func.count(Booking.id).label('booking_count')).join(Booking).filter(
            Booking.status != 'cancelled').group_by(User.id).order_by(
                desc('booking_count')).limit(5).all()

    room_stats_query = db.session.query(
        Room.name,
        func.coalesce(
            func.sum(
                (func.julianday(Booking.end_time) -
                 func.julianday(Booking.start_time)) * 24), 0).label('total_hours')).outerjoin(
                    Booking, (Room.id == Booking.room_id) &
                    (Booking.start_time >= month_ago) &
                    (Booking.status != 'cancelled')).filter(
                        Room.is_active == True).group_by(Room.id).all()

    max_hours = 176  # 8h dziennie * 22 dni robocze

    room_utilization = [{
        'room':
        row.name,
        'hours':
        round(float(row.total_hours), 1),
        'utilization':
        round((float(row.total_hours) / max_hours) * 100, 1)
    } for row in room_stats_query]
    room_utilization.sort(key=lambda x: x['utilization'], reverse=True)

    return stats, upcoming, top_users, room_utilization


def get_dashboard_api_stats():
    stats = get_booking_statistics()
    stats.update(get_extended_statistics())
    return stats


def get_extended_statistics():
    """Dane dla wykresu departamentów, heatmapy i trendu 30 dni."""
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    month_ago = now - timedelta(days=29)

    departments = db.session.query(
        func.coalesce(User.department, "Brak").label("department"),
        func.count(Booking.id).label("count"),
    ).join(Booking).filter(Booking.status != "cancelled").group_by(
        User.department
    ).all()

    heatmap = db.session.query(
        extract("dow", Booking.start_time).label("weekday"),
        extract("hour", Booking.start_time).label("hour"),
        func.count(Booking.id).label("count"),
    ).filter(Booking.status != "cancelled").group_by(
        "weekday", "hour"
    ).all()

    trend = db.session.query(
        func.date(Booking.start_time).label("date"),
        func.count(Booking.id).label("count"),
    ).filter(
        Booking.status != "cancelled", Booking.start_time >= month_ago
    ).group_by(func.date(Booking.start_time)).order_by("date").all()

    trend_map = {str(row.date): row.count for row in trend}
    trend_data = []
    for offset in range(30):
        day = (month_ago + timedelta(days=offset)).date().isoformat()
        trend_data.append({"date": day, "count": trend_map.get(day, 0)})

    return {
        "departments": [
            {"department": row.department, "count": row.count}
            for row in departments
        ],
        "heatmap": [
            {
                "weekday": int(row.weekday),
                "hour": int(row.hour),
                "count": row.count,
            }
            for row in heatmap
        ],
        "trend": trend_data,
    }
