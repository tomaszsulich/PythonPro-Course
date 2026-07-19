from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Report
from .tasks import generate_report_task

@require_POST
def create_report(request):
    report = Report.objects.create(status="PENDING")
    
    # Przekazanie zadania do kolejki brokera (nie blokuje wykonania)
    generate_report_task.delay(report.id)
    
    return JsonResponse({
        "id": report.id,
        "status": report.status,
        "message": "Report generation started."
    }, status=202)

def check_report_status(request, report_id):
    try:
        report = Report.objects.get(id=report_id)
        return JsonResponse({"id": report.id, "status": report.status})
    except Report.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)