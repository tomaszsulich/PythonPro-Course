"""
Główny plik uruchamiający aplikację.
"""
from sqlalchemy import inspect
import random
from datetime import datetime, timedelta, timezone

from app import create_app
from app.models import Booking, Equipment, Room, User
from app.db import db

app = create_app()


@app.route("/test-db")
def test_db() -> str:
    """Testuje połączenie z bazą"""
    try:
        db.session.execute(db.text("SELECT 1"))
        return "Połączenie OK!"
    except Exception as e:
        return f"Błąd połączenia: {str(e)}"
    


# Surowe dane wejściowe
EQUIPMENT_DATA = [
    {
        "name": "Projektor",
        "icon": "projector"
    },
    {
        "name": "Tablica",
        "icon": "chalkboard"
    },
    {
        "name": "Wideokonferencja",
        "icon": "video"
    },
    {
        "name": "Klimatyzacja",
        "icon": "snowflake"
    },
    {
        "name": "Nagłośnienie",
        "icon": "volume-up"
    },
]

ROOMS_DATA = [
    {
        "name": "Sala A1",
        "capacity": 10,
        "floor": 1,
        "description": "Mała sala do spotkań zespołowych",
        "hourly_rate": 50,
        "equipment_names": ["Tablica", "Klimatyzacja"]
    },
    {
        "name": "Sala B2",
        "capacity": 20,
        "floor": 2,
        "description": "Średnia sala z projektorem",
        "hourly_rate": 80,
        "equipment_names": ["Projektor", "Wideokonferencja", "Klimatyzacja"]
    },
    {
        "name":
        "Sala Konferencyjna",
        "capacity":
        50,
        "floor":
        3,
        "description":
        "Duża sala na prezentacje",
        "hourly_rate":
        150,
        "equipment_names": [
            "Projektor", "Tablica", "Wideokonferencja", "Klimatyzacja",
            "Nagłośnienie"
        ]
    },
    {
        "name": "Pokój Kreatywny",
        "capacity": 8,
        "floor": 1,
        "description": "Sala do burzy mózgów z tablicami",
        "hourly_rate": 60,
        "equipment_names": ["Tablica"]
    },
    {
        "name": "Sala Spotkań",
        "capacity": 15,
        "floor": 2,
        "description": "Sala do spotkań z klientami",
        "hourly_rate": 70,
        "equipment_names": ["Projektor", "Klimatyzacja"]
    },
    {
        "name": "Sala Szkoleniowa",
        "capacity": 30,
        "floor": 3,
        "description": "Sala do szkoleń i warsztatów",
        "hourly_rate": 120,
        "equipment_names": ["Projektor", "Klimatyzacja"]
    },
    {
        "name": "Sala Prezentacyjna",
        "capacity": 40,
        "floor": 3,
        "description": "Sala do prezentacji i pokazów",
        "hourly_rate": 130,
        "equipment_names": ["Projektor", "Wideokonferencja", "Klimatyzacja"]
    },
    {
        "name": "Sala Spotkań Zarządu",
        "capacity": 12,
        "floor": 4,
        "description": "Ekskluzywna sala dla zarządu",
        "hourly_rate": 200,
        "equipment_names": ["Projektor", "Wideokonferencja", "Klimatyzacja"]
    },
    {
        "name": "Sala Testowa",
        "capacity": 5,
        "floor": 1,
        "description": "Sala do testów i eksperymentów",
        "hourly_rate": 30,
        "equipment_names": ["Projektor"]
    },
    {
        "name": "Sala Spotkań Zespołu",
        "capacity": 18,
        "floor": 2,
        "description": "Sala do spotkań zespołowych i burzy mózgów",
        "hourly_rate": 75,
        "equipment_names": ["Tablica", "Klimatyzacja"]
    },
]

USERS_DATA = [
    {
        "name": "Jan Kowalski",
        "email": "jan@firma.pl",
        "department": "IT",
        "is_admin": False
    },
    {
        "name": "Anna Nowak",
        "email": "anna@firma.pl",
        "department": "HR",
        "is_admin": False
    },
    {
        "name": "Piotr Wiśniewski",
        "email": "piotr@firma.pl",
        "department": "Marketing",
        "is_admin": False
    },
    {
        "name": "Maria Dąbrowska",
        "email": "maria@firma.pl",
        "department": "IT",
        "is_admin": True
    },
    {
        "name": "Krzysztof Zieliński",
        "email": "krzysztof@firma.pl",
        "department": "Finanse",
        "is_admin": False
    },
    {
        "name": "Ewa Kaczmarek",
        "email": "ewa@firma.pl",
        "department": "Marketing",
        "is_admin": False
    },
    {
        "name": "Tomasz Lewandowski",
        "email": "tomasz@firma.pl",
        "department": "IT",
        "is_admin": False
    },
    {
        "name": "Agnieszka Wójcik",
        "email": "agata@firma.pl",
        "department": "HR",
        "is_admin": False
    },
    {
        "name": "Michał Kamiński",
        "email": "michal@firma.pl",
        "department": "IT",
        "is_admin": False
    },
    {
        "name": "Joanna Szymańska",
        "email": "joanna@firma.pl",
        "department": "HR",
        "is_admin": False
    },
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


def seed_database():
    """Wypełnia bazę przykładowymi danymi."""
    with app.app_context():
        if User.query.first():
            return

        # Wczytywanie wyposażenia
        equipments_map = {}
        for eq_data in EQUIPMENT_DATA:
            eq = Equipment(name=eq_data["name"], icon=eq_data["icon"])
            db.session.add(eq)
            equipments_map[eq_data["name"]] = eq

        db.session.commit()

        # Wczytywanie sal i mapowanie relacji
        rooms = []
        for room_data in ROOMS_DATA:
            room = Room(name=room_data["name"],
                        capacity=room_data["capacity"],
                        floor=room_data["floor"],
                        description=room_data["description"],
                        hourly_rate=room_data["hourly_rate"])
            # Powiązanie sprzętu na podstawie słownika
            room.equipment = [
                equipments_map[name] for name in room_data["equipment_names"]
            ]
            db.session.add(room)
            rooms.append(room)

        # Wczytywanie użytkowników
        users = []
        for user_data in USERS_DATA:
            user = User(**user_data)
            db.session.add(user)
            users.append(user)

        db.session.commit()

        # Generowanie rezerwacji
        now = datetime.now(timezone.utc).replace(minute=0,
                                                 second=0,
                                                 microsecond=0)

        for _ in range(1000):
            room = random.choice(rooms)
            user = random.choice(users)

            days_offset = random.randint(0, 14)
            hour = random.randint(9, 16)
            duration = random.choice([1, 2, 3])

            start = now + timedelta(days=days_offset, hours=hour - now.hour)
            end = start + timedelta(hours=duration)

            if room.is_available(start, end):
                booking = Booking(room_id=room.id,
                                  user_id=user.id,
                                  title=random.choice(BOOKING_TITLES),
                                  start_time=start,
                                  end_time=end,
                                  attendees_count=random.randint(
                                      2, room.capacity),
                                  applied_hourly_rate=room.hourly_rate)
                db.session.add(booking)

        db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        # Sprawdzenie czy tabele już istnieją, aby uniknąć ponownego tworzenia

        inspector = inspect(db.engine)
        if not inspector.has_table("rooms"):  # Sprawdź dowolną tabelę bazową
            print("Inicjalizacja nowej bazy danych...")
            db.create_all()
            seed_database()
        else:
            print("Baza danych już istnieje. Pomijam inicjalizację.")

    app.run(debug=False, port=5000)
