import random
from datetime import datetime, timedelta

from app import create_app
from app.db import db
from app.models import Booking, Equipment, Room, User


app = create_app()

EQUIPMENT_DATA = [
    ("Projektor", "projector"),
    ("Tablica", "chalkboard"),
    ("Wideokonferencja", "video"),
    ("Klimatyzacja", "snowflake"),
    ("Nagłośnienie", "volume-up"),
]

ROOM_DATA = [
    (
        "Sala A1",
        10,
        1,
        "Mała sala do spotkań zespołowych",
        50,
        ["Tablica", "Klimatyzacja"],
    ),
    (
        "Sala B2",
        20,
        2,
        "Średnia sala z projektorem",
        80,
        ["Projektor", "Wideokonferencja", "Klimatyzacja"],
    ),
    (
        "Sala Konferencyjna",
        50,
        3,
        "Duża sala na prezentacje",
        150,
        [
            "Projektor",
            "Tablica",
            "Wideokonferencja",
            "Klimatyzacja",
            "Nagłośnienie",
        ],
    ),
    (
        "Pokój Kreatywny",
        8,
        1,
        "Sala do burzy mózgów z tablicami",
        60,
        ["Tablica"],
    ),
]

USER_DATA = [
    ("Jan Kowalski", "jan@firma.pl", "IT", False),
    ("Anna Nowak", "anna@firma.pl", "HR", False),
    ("Piotr Wiśniewski", "piotr@firma.pl", "Marketing", False),
    ("Maria Dąbrowska", "maria@firma.pl", "IT", True),
]

BOOKING_TITLES = [
    "Spotkanie zespołu",
    "Code review",
    "Prezentacja projektu",
    "Rozmowa rekrutacyjna",
    "Szkolenie",
    "Planning sprint",
    "Retrospektywa",
    "Demo dla klienta",
]

ROOM_WEIGHTS = [20, 30, 35, 15]
USER_WEIGHTS = [35, 20, 25, 20]
HOURS = [9, 10, 11, 12, 13, 14, 15, 16]
HOUR_WEIGHTS = [4, 8, 10, 7, 5, 8, 5, 3]
DURATIONS = [1, 2, 3]
DURATION_WEIGHTS = [65, 25, 10]


def seed_equipment():
    equipment_map = {}

    for equipment_name, equipment_icon in EQUIPMENT_DATA:
        equipment = Equipment(
            name=equipment_name,
            icon=equipment_icon,
        )
        equipment_map[equipment_name] = equipment
        db.session.add(equipment)

    return equipment_map


def seed_rooms(equipment_map):
    rooms = []

    for (
        room_name,
        capacity,
        floor,
        description,
        hourly_rate,
        equipment_names,
    ) in ROOM_DATA:
        room = Room(
            name=room_name,
            capacity=capacity,
            floor=floor,
            description=description,
            hourly_rate=hourly_rate,
        )
        room.equipment = [
            equipment_map[equipment_name]
            for equipment_name in equipment_names
        ]
        rooms.append(room)
        db.session.add(room)

    return rooms


def seed_users():
    users = []

    for user_name, email, department, is_admin in USER_DATA:
        user = User(
            name=user_name,
            email=email,
            department=department,
            is_admin=is_admin,
        )
        users.append(user)
        db.session.add(user)

    return users


def add_booking(rooms, users, booking_date):
    selected_room = random.choices(
        rooms,
        weights=ROOM_WEIGHTS,
        k=1,
    )[0]
    selected_user = random.choices(
        users,
        weights=USER_WEIGHTS,
        k=1,
    )[0]
    selected_hour = random.choices(
        HOURS,
        weights=HOUR_WEIGHTS,
        k=1,
    )[0]
    duration_hours = random.choices(
        DURATIONS,
        weights=DURATION_WEIGHTS,
        k=1,
    )[0]

    start_time = booking_date.replace(
        hour=selected_hour,
        minute=random.choice([0, 30]),
        second=0,
        microsecond=0,
    )
    end_time = start_time + timedelta(hours=duration_hours)

    if not selected_room.is_available(start_time, end_time):
        return False

    db.session.add(
        Booking(
            room=selected_room,
            user=selected_user,
            title=random.choice(BOOKING_TITLES),
            start_time=start_time,
            end_time=end_time,
            attendees_count=random.randint(2, selected_room.capacity),
            applied_hourly_rate=selected_room.hourly_rate,
        )
    )
    return True


def seed_period(rooms, users, start_date, number_of_days):
    created_count = 0

    for day_offset in range(number_of_days):
        booking_date = start_date + timedelta(days=day_offset)
        target_count = (
            random.randint(5, 10)
            if booking_date.weekday() < 5
            else random.randint(1, 3)
        )
        daily_created = 0
        attempts = 0

        while (
            daily_created < target_count
            and attempts < target_count * 6
        ):
            if add_booking(rooms, users, booking_date):
                daily_created += 1
                created_count += 1

            attempts += 1

    return created_count


def seed_database():
    with app.app_context():
        if User.query.first():
            print("Baza już zawiera dane. Pomijam seeding.")
            return

        print("Tworzenie przykładowych danych...")
        random.seed(42)

        equipment_map = seed_equipment()
        rooms = seed_rooms(equipment_map)
        users = seed_users()
        db.session.flush()

        today = datetime.now().replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        )

        dashboard_count = seed_period(
            rooms,
            users,
            today - timedelta(days=29),
            30,
        )
        report_count = seed_period(
            rooms,
            users,
            datetime(2024, 1, 1),
            31,
        )

        db.session.commit()

        print("✅ Baza danych wypełniona przykładowymi danymi!")
        print(
            f"Utworzono {dashboard_count} rezerwacji dla dashboardu "
            f"oraz {report_count} rezerwacji dla raportu 2024-01."
        )


if __name__ == "__main__":
    seed_database()
