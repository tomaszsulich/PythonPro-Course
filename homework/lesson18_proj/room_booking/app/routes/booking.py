from flask import Blueprint, request, jsonify
from .utils import http_err
from ..validators.booking_validator import validate_booking_payload
from ..services import booking_service as bs

bookings_bp = Blueprint("bookings", __name__, url_prefix="/api/bookings")


@bookings_bp.route("/", methods=["GET"])
def get_bookings():
    filters = {
        "room_id": request.args.get("room_id"),
        "user_id": request.args.get("user_id"),
        "status": request.args.get("status"),
        "date": request.args.get("date")
    }
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 20, type=int)

    try:
        pagination = bs.get_bookings_list(filters, page, per_page)
    except ValueError as e:
        return http_err(str(e), 400)

    return jsonify({
        "bookings": [
            b.to_dict(include_room=True, include_user=True)
            for b in pagination.items
        ],
        "total":
        pagination.total,
        "pages":
        pagination.pages,
    })


@bookings_bp.route("/", methods=["POST"])
def create_booking():
    data = request.get_json() or {}

    parsed_data, err = validate_booking_payload(data)
    if err:
        return http_err(err, 400)

    try:
        booking = bs.create_booking(parsed_data)
        return jsonify({
            "message": "Rezerwacja utworzona",
            "booking": booking.to_dict(include_room=True),
        }), 201
    except ValueError as e:
        return http_err(str(e), 400)
    except Exception as e:
        return http_err(f"Błąd wewnętrzny: {str(e)}", 500)


@bookings_bp.route("/series", methods=["POST"])
def create_series():
    data = request.get_json() or {}
    parsed_data, err = validate_booking_payload(data)
    if err:
        return http_err(err, 400)
    try:
        bookings = bs.create_booking_series(parsed_data)
        return jsonify({
            "message": "Seria rezerwacji utworzona",
            "series_id": bookings[0].series_id,
            "bookings": [booking.to_dict() for booking in bookings],
        }), 201
    except ValueError as exc:
        return http_err(str(exc), 400)


@bookings_bp.route("/<int:booking_id>", methods=["DELETE"])
def cancel_booking(booking_id):
    try:
        if request.args.get("scope") == "series":
            bs.cancel_booking_series(booking_id)
        else:
            bs.cancel_booking(booking_id)
        return jsonify({"message": "Rezerwacja anulowana"})
    except ValueError as e:
        return http_err(str(e), 400)
    except Exception as e:
        return http_err(str(e), 500)


@bookings_bp.route("/available-rooms", methods=["GET"])
def find_available_rooms():
    start_time = request.args.get("start_time")
    end_time = request.args.get("end_time")

    if not start_time or not end_time:
        return http_err("Brakuje wymaganych parametrów daty", 400)

    capacity = request.args.get("capacity", 1, type=int)
    equipment = None
    if eq_param := request.args.get("equipment"):
        equipment = [e.strip() for e in eq_param.split(",")]

    try:
        rooms, s_time, e_time = bs.search_available_rooms(
            start_time, end_time, capacity, equipment)
    except ValueError as e:
        return http_err(str(e), 400)

    return jsonify({
        "available_rooms": [r.to_dict() for r in rooms],
        "search_criteria": {
            "start_time": s_time.isoformat(),
            "end_time": e_time.isoformat(),
            "min_capacity": capacity,
            "required_equipment": equipment,
        },
    })
