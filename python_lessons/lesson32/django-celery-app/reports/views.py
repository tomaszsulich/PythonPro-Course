from json import JSONDecodeError

from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Report, Ping
from .tasks.email_tasks import generate_report_task


@csrf_exempt
@require_POST
def create_report(request):
    report = Report.objects.create(status="PENDING")
    
    # Przekazanie zadania do kolejki brokera - żądanie HTTP nie czeka
    # na zakończenie generowania raportu.
    generate_report_task.delay(report.id)
    
    return JsonResponse(
    {
        "id": report.id,
        "status": report.status,
        "message": "Report generation started."
    }, 
    status=202)


@require_GET
def get_report(request, report_id: int):
    # Funkcja została rozpoczęta, ale jej implementacja nie była widoczna
    # w materiale kursowym, dlatego została dokończona samodzielnie.
    attrs = (
        "id",
        "status",
    )
    
    try:
        report = Report.objects.values(*attrs).get(id=report_id)
    except Report.DoesNotExist:
        return JsonResponse(
            {
                "error": "Report not found.",
            },
            status=404,
        )
    return JsonResponse(report)


@require_GET
def get_pings(request):
    pings = list(
        Ping.objects.values(
            "id",
            "created_at",
        )
    )
    
    return JsonResponse(
        {"pings": pings}, safe=False
    )