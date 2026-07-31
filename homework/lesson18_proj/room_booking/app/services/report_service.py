import io
import os

from calendar import monthrange
from datetime import datetime

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Image,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)
from sqlalchemy import desc, func

from ..db import db
from ..models import Booking, Room, User


def _find_font(*paths):
    for path in paths:
        if os.path.exists(path):
            return path
    raise RuntimeError("Nie znaleziono czcionki obsługującej polskie znaki.")


FONT_REGULAR = _find_font(
    r"C:\Windows\Fonts\arial.ttf",
    "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/Library/Fonts/Arial.ttf",
)
FONT_BOLD = _find_font(
    r"C:\Windows\Fonts\arialbd.ttf",
    "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/Library/Fonts/Arial Bold.ttf",
)

pdfmetrics.registerFont(TTFont("ReportFont", FONT_REGULAR))
pdfmetrics.registerFont(TTFont("ReportFont-Bold", FONT_BOLD))


def _parse_month(month):
    try:
        year, month_number = map(int, month.split("-"))
        start = datetime(year, month_number, 1)
        end = datetime(
            year,
            month_number,
            monthrange(year, month_number)[1],
            23,
            59,
            59,
        )
        return start, end
    except (ValueError, AttributeError):
        raise ValueError("Parametr month musi mieć format YYYY-MM.")


def _table(data, column_widths):
    table = Table(data, colWidths=column_widths, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8EEF7")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#1F2937")),
                ("FONTNAME", (0, 0), (-1, 0), "ReportFont-Bold"),
                ("FONTNAME", (0, 1), (-1, -1), "ReportFont"),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("ALIGN", (1, 1), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#B8C2CC")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return table


def _build_utilization_chart(room_rows):
    chart = io.BytesIO()

    room_names = [row.name for row in room_rows]
    hours = [float(row.hours or 0) for row in room_rows]

    fig, ax = plt.subplots(figsize=(8.2, 4.5))

    if room_names:
        bars = ax.barh(room_names[::-1], hours[::-1])
        ax.set_xlabel("Łączny czas rezerwacji [h]")
        ax.set_title("Wykorzystanie sal w wybranym miesiącu")
        ax.grid(axis="x", alpha=0.25)

        max_value = max(hours) if hours else 0
        offset = max(max_value * 0.015, 0.05)
        for bar, value in zip(bars, hours[::-1]):
            ax.text(
                bar.get_width() + offset,
                bar.get_y() + bar.get_height() / 2,
                f"{value:.1f} h",
                va="center",
                fontsize=9,
            )
        ax.set_xlim(0, max_value * 1.18 if max_value else 1)
    else:
        ax.text(
            0.5,
            0.5,
            "Brak rezerwacji w wybranym miesiącu",
            ha="center",
            va="center",
            transform=ax.transAxes,
        )
        ax.set_axis_off()

    fig.tight_layout()
    fig.savefig(chart, format="png", dpi=160, bbox_inches="tight")
    plt.close(fig)
    chart.seek(0)
    return chart


def build_monthly_report(month):
    start, end = _parse_month(month)

    base_filter = (
        Booking.start_time >= start,
        Booking.start_time <= end,
        Booking.status != "cancelled",
    )

    bookings = Booking.query.filter(*base_filter).all()
    total_hours = sum(booking.duration_hours for booking in bookings)
    revenue = sum(booking.total_cost for booking in bookings)

    duration_expression = (
        func.julianday(Booking.end_time) - func.julianday(Booking.start_time)
    ) * 24

    top_rooms = (
        db.session.query(
            Room.name,
            func.count(Booking.id).label("count"),
            func.sum(duration_expression).label("hours"),
        )
        .join(Booking)
        .filter(*base_filter)
        .group_by(Room.id, Room.name)
        .order_by(desc("hours"), desc("count"))
        .limit(10)
        .all()
    )

    top_users = (
        db.session.query(
            User.name,
            func.count(Booking.id).label("count"),
            func.sum(duration_expression).label("hours"),
        )
        .join(Booking)
        .filter(*base_filter)
        .group_by(User.id, User.name)
        .order_by(desc("count"), desc("hours"))
        .limit(10)
        .all()
    )

    utilization_chart = _build_utilization_chart(top_rooms)

    output = io.BytesIO()
    document = SimpleDocTemplate(
        output,
        pagesize=A4,
        rightMargin=1.6 * cm,
        leftMargin=1.6 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
        title=f"Raport miesięczny {month}",
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        fontName="ReportFont-Bold",
        fontSize=20,
        leading=24,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1F2937"),
        spaceAfter=12,
    )
    heading_style = ParagraphStyle(
        "ReportHeading",
        parent=styles["Heading2"],
        fontName="ReportFont-Bold",
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#1F2937"),
        spaceBefore=4,
        spaceAfter=8,
    )
    body_style = ParagraphStyle(
        "ReportBody",
        parent=styles["BodyText"],
        fontName="ReportFont",
        fontSize=10,
        leading=14,
    )

    summary_data = [
        ["Liczba rezerwacji", "Łączny czas", "Przychód"],
        [str(len(bookings)), f"{total_hours:.1f} h", f"{revenue:.2f} zł"],
    ]
    summary_table = Table(summary_data, colWidths=[5.7 * cm] * 3)
    summary_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8EEF7")),
                ("FONTNAME", (0, 0), (-1, 0), "ReportFont-Bold"),
                ("FONTNAME", (0, 1), (-1, 1), "ReportFont-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 9),
                ("FONTSIZE", (0, 1), (-1, 1), 14),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#B8C2CC")),
                ("INNERGRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#D1D5DB")),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ]
        )
    )

    room_data = [["Sala", "Rezerwacje", "Łączny czas"]]
    room_data.extend(
        [[row.name, row.count, f"{float(row.hours or 0):.1f} h"] for row in top_rooms]
    )
    if len(room_data) == 1:
        room_data.append(["Brak danych", "-", "-"])

    user_data = [["Użytkownik", "Rezerwacje", "Łączny czas"]]
    user_data.extend(
        [[row.name, row.count, f"{float(row.hours or 0):.1f} h"] for row in top_users]
    )
    if len(user_data) == 1:
        user_data.append(["Brak danych", "-", "-"])

    elements = [
        Paragraph(f"Raport miesięczny - {month}", title_style),
        Paragraph(
            f"Okres raportu: {start.strftime('%d.%m.%Y')} - {end.strftime('%d.%m.%Y')}",
            body_style,
        ),
        Spacer(1, 0.45 * cm),
        Paragraph("Podsumowanie", heading_style),
        summary_table,
        Spacer(1, 0.55 * cm),
        Paragraph("Top 10 sal", heading_style),
        _table(room_data, [9.2 * cm, 4.0 * cm, 4.0 * cm]),
        Spacer(1, 0.55 * cm),
        Paragraph("Top 10 użytkowników", heading_style),
        _table(user_data, [9.2 * cm, 4.0 * cm, 4.0 * cm]),
        PageBreak(),
        Paragraph("Wykorzystanie sal", heading_style),
        Paragraph(
            "Wykres przedstawia łączny czas rezerwacji każdej sali w wybranym miesiącu.",
            body_style,
        ),
        Spacer(1, 0.25 * cm),
        Image(utilization_chart, width=17.2 * cm, height=9.4 * cm),
    ]

    document.build(elements)
    output.seek(0)
    return output
