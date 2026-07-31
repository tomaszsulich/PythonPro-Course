import time
from typing import Any

from flask import Blueprint, Response, jsonify
from sqlalchemy import event
from sqlalchemy.orm import joinedload

from ..db import db
from ..models import Booking, Room, User


performance_bp = Blueprint("performance", __name__)

query_count = 0


def register_query_counter() -> None:
    """Rejestruje nasłuchiwanie zdarzeń SQLAlchemy do zliczania zapytań SQL."""
    
    # SQLAlchemy wywoła tę funkcję przed każdym zapytaniem SQL
    @event.listens_for(db.engine, "before_cursor_execute")
    def count_queries(conn: Any, cursor: Any, statement: str, parameters: Any, context: Any, executemany: bool) -> None:
        """Liczy wykonane zapytania SQL"""
        global query_count
        query_count += 1

 
@performance_bp.route("/debug/n-plus-1")
def demo_n_plus_1() -> Response:
    """Pokazuje problem N+1 oraz optymalizację za pomocą joinedload."""
    global query_count
    
    query_count = 0
    start = time.time()
    
    bookings = Booking.query.all()
    
    bad_result = []
    for booking in bookings:
        room = Room.query.get(booking.room_id)
        user = User.query.get(booking.user_id)
        
        bad_result.append({
            "title": booking.title,
            "room": room.name if room else None,
            "user": user.name if user else None,
        })
        
    bad_time = time.time() - start
    bad_queries = query_count
    
    query_count = 0
    start = time.time()
    
    bookings = (
        Booking.query.options(
            joinedload(Booking.room),
            joinedload(Booking.user),
        ).all()
    )
    
    good_result = []
    for booking in bookings:
        good_result.append({
            "title": booking.title,
            "room": booking.room.name if booking.room else None,
            "user": booking.user.name if booking.user else None,
        })
        
    good_time = time.time() - start
    good_queries = query_count
    
    return jsonify({
        "without_optimization": {
            "query_count": bad_queries,
            "time_ms": round(bad_time * 1000, 2),
            "bookings": bad_result,
        },
        "with_joinedload": {
            "query_count": good_queries,
            "time_ms": round(good_time * 1000, 2),
            "bookings": good_result
        },
    })