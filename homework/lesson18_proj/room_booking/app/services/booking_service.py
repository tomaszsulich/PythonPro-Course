from datetime import datetime, timedelta, timezone
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from ..db import db
from ..models import Room, User, Booking, Equipment


def check_room_availability(room_id: int,
                            start_time: datetime,
                            end_time: datetime,
                            exclude_booking_id: int = None) -> bool:
    """Sprawdza dostępność sali w bazie danych (przeniesione z modelu Room)."""
    query = Booking.query.filter(Booking.room_id == room_id, Booking.status
                                 != 'cancelled', Booking.start_time < end_time,
                                 Booking.end_time > start_time)

    if exclude_booking_id:
        query = query.filter(Booking.id != exclude_booking_id)

    return query.count() == 0


def find_available_rooms(start_time: datetime,
                         end_time: datetime,
                         min_capacity: int = 1,
                         required_equipment: list = None):
    """Wyszukuje wolne pokoje spełniające kryteria (przeniesione z models/utils.py)."""
    query = Room.query.options(joinedload(Room.equipment)).filter(
        Room.is_active == True, Room.capacity >= min_capacity)

    if required_equipment:
        equip_count = len(required_equipment)
        query = query.join(Room.equipment).\
            filter(Equipment.name.in_(required_equipment)).\
            group_by(Room.id).\
            having(func.count(Equipment.id) == equip_count)

    candidate_rooms = query.all()

    # Filtrowanie po dostępności czasowej za pomocą funkcji wewnętrznej serwisu
    return [
        room for room in candidate_rooms
        if check_room_availability(room.id, start_time, end_time)
    ]


def get_bookings_list(filters: dict, page: int = 1, per_page: int = 20):
    query = Booking.query.options(joinedload(Booking.room),
                                  joinedload(Booking.user))

    if room_id := filters.get("room_id"):
        query = query.filter(Booking.room_id == room_id)
    if user_id := filters.get("user_id"):
        query = query.filter(Booking.user_id == user_id)
    if status := filters.get("status"):
        query = query.filter(Booking.status == status)
    if date_str := filters.get("date"):
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
            query = query.filter(func.date(Booking.start_time) == date_obj)
        except ValueError:
            raise ValueError("Niepoprawny format daty (oczekiwany YYYY-MM-DD)")

    query = query.order_by(Booking.start_time.desc())
    return query.paginate(page=page, per_page=per_page)


def create_booking(data: dict):
    room = Room.query.get(data['room_id'])
    if not room:
        raise ValueError("Pokój z tym ID nie istnieje.")
    if not room.is_active:
        raise ValueError("Pokój jest nieaktywny.")
    if not User.query.get(data['user_id']):
        raise ValueError("Użytkownik o tym ID nie istnieje.")
    if len(data['title']) < 3:
        raise ValueError("Tytuł jest za krótki (min. 3 znaki).")

    attendees = data.get('attendees_count', 1)
    if room.capacity < attendees:
        raise ValueError(
            "Pojemność sali jest zbyt mała dla tej liczby uczestników.")

    # Użycie funkcji serwisowej zamiast metody modelu
    if not check_room_availability(room.id, data['start_time'],
                                   data['end_time']):
        raise ValueError("Pokój jest zajęty w wybranym terminie.")

    booking = Booking(room_id=room.id,
                      user_id=data['user_id'],
                      title=data['title'],
                      description=data.get('description'),
                      start_time=data['start_time'],
                      end_time=data['end_time'],
                      attendees_count=attendees,
                      applied_hourly_rate=room.hourly_rate)
    db.session.add(booking)
    db.session.commit()
    return booking


def cancel_booking(booking_id: int):
    booking = Booking.query.get(booking_id)
    if not booking:
        raise ValueError("Rezerwacja nie istnieje.")
    if booking.status == "cancelled":
        raise ValueError("Rezerwacja już anulowana.")

    s_time = booking.start_time
    if s_time.tzinfo is None:
        s_time = s_time.replace(tzinfo=timezone.utc)

    if s_time < datetime.now(timezone.utc):
        raise ValueError("Nie można anulować przeszłej rezerwacji.")

    booking.status = "cancelled"
    db.session.commit()
    return booking


def search_available_rooms(start_time_str, end_time_str, capacity,
                           equipment_list):
    try:
        start_time = datetime.fromisoformat(start_time_str)
        end_time = datetime.fromisoformat(end_time_str)
    except ValueError:
        raise ValueError("Wymagane parametry w poprawnym formacie ISO.")

    rooms = find_available_rooms(start_time, end_time, capacity,
                                 equipment_list)
    return rooms, start_time, end_time


def create_booking_series(data: dict):
    from dateutil.rrule import WEEKLY, rrule
    import uuid

    rule = data.get("recurrence_rule")
    if rule not in {"WEEKLY", "BIWEEKLY"}:
        raise ValueError("recurrence_rule musi mieć wartość WEEKLY lub BIWEEKLY.")

    months = int(data.get("months", 3))
    if months < 1:
        raise ValueError("months musi być większe od 0.")

    interval = 1 if rule == "WEEKLY" else 2
    until = data["start_time"] + timedelta(days=months * 30)
    starts = list(rrule(WEEKLY, dtstart=data["start_time"], until=until,
                        interval=interval))
    duration = data["end_time"] - data["start_time"]

    for start in starts:
        if not check_room_availability(data["room_id"], start, start + duration):
            raise ValueError(f"Konflikt rezerwacji dla terminu {start.isoformat()}.")

    room = db.session.get(Room, data["room_id"])
    if not room or not room.is_active:
        raise ValueError("Pokój nie istnieje lub jest nieaktywny.")
    if not db.session.get(User, data["user_id"]):
        raise ValueError("Użytkownik o tym ID nie istnieje.")
    if len(data["title"]) < 3:
        raise ValueError("Tytuł jest za krótki (min. 3 znaki).")
    if room.capacity < data.get("attendees_count", 1):
        raise ValueError("Pojemność sali jest zbyt mała.")

    series_id = str(uuid.uuid4())
    bookings = []
    for start in starts:
        booking = Booking(
            room_id=room.id,
            user_id=data["user_id"],
            title=data["title"],
            description=data.get("description"),
            start_time=start,
            end_time=start + duration,
            attendees_count=data.get("attendees_count", 1),
            applied_hourly_rate=room.hourly_rate,
            recurrence_rule=rule,
            series_id=series_id,
        )
        db.session.add(booking)
        bookings.append(booking)

    db.session.commit()
    return bookings


def cancel_booking_series(booking_id: int):
    booking = db.session.get(Booking, booking_id)
    if not booking:
        raise ValueError("Rezerwacja nie istnieje.")
    if not booking.series_id:
        return cancel_booking(booking_id)

    Booking.query.filter_by(series_id=booking.series_id).update(
        {"status": "cancelled"}, synchronize_session=False
    )
    db.session.commit()
