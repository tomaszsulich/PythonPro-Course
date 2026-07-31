from flask import Blueprint, jsonify

from ..services import notification_service as ns
from .utils import http_err

notifications_bp = Blueprint("notifications", __name__, url_prefix="/api/notifications")


@notifications_bp.route("", methods=["GET"])
def get_notifications():
    notifications = ns.get_unread_notifications()
    return jsonify([notification.to_dict() for notification in notifications])


@notifications_bp.route("/<int:notification_id>/read", methods=["POST"])
def read_notification(notification_id):
    try:
        notification = ns.mark_as_read(notification_id)
        return jsonify(notification.to_dict())
    except ValueError as exc:
        return http_err(str(exc), 404)
