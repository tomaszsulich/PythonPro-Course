from flask import Blueprint, request, send_file

from ..services.report_service import build_monthly_report
from .utils import http_err

reports_bp = Blueprint("reports", __name__, url_prefix="/api/reports")


@reports_bp.route("/monthly", methods=["GET"])
def monthly_report():
    try:
        pdf = build_monthly_report(request.args.get("month"))
    except ValueError as exc:
        return http_err(str(exc), 400)

    return send_file(
        pdf,
        mimetype="application/pdf",
        as_attachment=True,
        download_name="monthly-report.pdf",
    )
