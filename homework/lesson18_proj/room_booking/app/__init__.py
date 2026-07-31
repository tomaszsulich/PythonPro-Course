from flask import Flask
from sqlalchemy import inspect, text
from .db import db
from .routes import BLUEPRINTS
# Import modeli jest konieczny, aby db.create_all() wykryło tabele
from .models import Room, Booking, Equipment, User, Notification


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'twoj-tajny-klucz'

    # Inicjalizacja rozszerzeń
    db.init_app(app)

    # Rejestracja Blueprintów

    for bp in BLUEPRINTS:
        app.register_blueprint(bp)

    with app.app_context():
        db.create_all()

        columns = {column["name"] for column in inspect(db.engine).get_columns("bookings")}
        if "recurrence_rule" not in columns:
            db.session.execute(text("ALTER TABLE bookings ADD COLUMN recurrence_rule VARCHAR(20)"))
        if "series_id" not in columns:
            db.session.execute(text("ALTER TABLE bookings ADD COLUMN series_id VARCHAR(36)"))
            db.session.execute(text("CREATE INDEX IF NOT EXISTS ix_bookings_series_id ON bookings (series_id)"))
        db.session.commit()

    return app
