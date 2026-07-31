import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")
    SQLALCHEMY_DATABASE_URI = "sqlite:///room_booking.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
