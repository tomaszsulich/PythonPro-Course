import time
from celery import shared_task
from ..models import Report, Ping


@shared_task
def generate_report_task(report_id):
    try:
        report = Report.objects.get(id=report_id)
    except Report.DoesNotExist:
        return

    # Zmiana statusu na uruchomiony
    report.status = "RUNNING"
    report.save(update_fields=["status"])

    # Symulacja ciężkiej pracy (np. generowanie pliku, agregacja danych)
    time.sleep(10)

    # Zakończenie pracy
    report.status = "SUCCESS"
    report.save(update_fields=["status"])
    
    
@shared_task
def system_ping():
    try:
        Ping.objects.create()
    except Exception:
        ...