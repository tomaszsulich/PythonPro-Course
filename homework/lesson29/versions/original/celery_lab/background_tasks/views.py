from celery import chain
from celery.result import AsyncResult
from django.conf import settings
from django.db import transaction
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from .models import EmailNotification, UploadedImage
from .tasks import (
    classify_image,
    generate_random_number,
    generate_users_csv,
    hello_world,
    multiply,
    multiply_by_ten,
    process_video,
    save_result_to_file,
    send_email_notification,
    send_priority_email,
    simulate_cpu_bound_task,
    track_progress,
)


@transaction.atomic
def create_email_notification_view(request: HttpRequest):
    notification = EmailNotification.objects.create(
        recipient_email='anna.kowalska@gmail.com',
        subject='Powiadomienie transakcyjne',
        body='Wiadomość utworzona w ramach transakcji.'
    )

    transaction.on_commit(
        lambda: send_email_notification.delay(notification.id)
    )

    return JsonResponse({
        "message": "Powiadomienie zostało utworzone.",
        "notification_id": notification.id,
    })


def csv_report_status_view(request: HttpRequest, task_id: str):
    task = AsyncResult(task_id)

    response = {
        "task_id": task_id,
        "state": task.state,
    }

    if task.state == 'SUCCESS':
        response["download_url"] = f"{settings.MEDIA_URL}{task.result}"

    return JsonResponse(response)


def generate_report_view(request: HttpRequest):
    # Wywołujemy zadanie w tle.
    # .delay() to skrót do .apply_async().
    # Aplikacja nie czeka na zakończenie zadania.
    task = simulate_cpu_bound_task.delay(20) # symulacja 20-sekundowego zadania

    # Zwracamy natychmiastową odpowiedź do użytkownika.
    # task.id to unikalny identyfikator zadania, który możemy zapisać
    # i użyć później do sprawdzenia statusu.
    return JsonResponse({
        "message": (
            "Twoje żądanie generowania raportu zostało przyjęte "
            "i jest przetwarzane w tle."
        ),
        "task_id": task.id,
    })


def generate_users_csv_view(request: HttpRequest):
    task = generate_users_csv.delay()

    return JsonResponse({
        "task_id": task.id,
    })


def hello_world_view(request: HttpRequest):
    task = hello_world.delay()

    return JsonResponse({
        "message": "Zadanie Hello World zostało przekazane do Celery.",
        "task_id": task.id,
    })


def image_result_view(request: HttpRequest, image_id: int) -> JsonResponse:
    uploaded_image = UploadedImage.objects.get(pk=image_id)

    return JsonResponse({
        "image_id": uploaded_image.id,
        "classification_result": uploaded_image.classification_result,
        "image_type": uploaded_image.image_type,
        "image_format": uploaded_image.image_format,
        "image_mode": uploaded_image.image_mode,
        "width": uploaded_image.width,
        "height": uploaded_image.height,
        "orientation": uploaded_image.orientation,
        "pixel_count": uploaded_image.pixel_count,
        "has_alpha": uploaded_image.has_alpha,
    })


def multiply_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        a = float(request.POST['a'])
        b = float(request.POST['b'])

        task = multiply.delay(a, b)

        return JsonResponse({
            "message": "Zadanie mnożenia zostało przekazane do Celery.",
            "task_id": task.id,
        })

    return render(request, 'multiply.html')


def process_video_view(request: HttpRequest):
    task = process_video.delay()

    return JsonResponse({
        "message": "Przetwarzanie wideo rozpoczęte!",
        "task_id": task.id,
    })


def send_priority_email_view(request: HttpRequest):
    task = send_priority_email.delay('anna.kowalska@gmail.com')

    return JsonResponse({
        "message": "Priorytetowy mail został przekazany do kolejki.",
        "task_id": task.id,
    })


def start_chain_view(request: HttpRequest):
    workflow = chain(
        generate_random_number.s(),
        multiply_by_ten.s(),
        save_result_to_file.s(),
    )

    task = workflow.apply_async()

    return JsonResponse({
        "message": "Łańcuch zadań został uruchomiony.",
        "task_id": task.id,
    })


def start_progress_task_view(request: HttpRequest):
    task = track_progress.delay()

    return JsonResponse({
        "message": "Zadanie zostało uruchomione.",
        "task_id": task.id,
    })


def task_status_view(request: HttpRequest, task_id: str):
    task = AsyncResult(task_id)

    response = {
        "task_id": task_id,
        "state": task.state,
    }

    if task.state == 'PROGRESS':
        response.update({
            "current": task.info.get('current', 0),
            "total": task.info.get('total', 100),
        })
    elif task.state == 'SUCCESS':
        response["result"] = task.result

    return JsonResponse(response)


def upload_image_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        uploaded_image = UploadedImage.objects.create(
            image=request.FILES['image'],
        )

        task = classify_image.delay(uploaded_image.id)

        return JsonResponse({
            "message": "Obraz został przesłany do klasyfikacji.",
            "image_id": uploaded_image.id,
            "task_id": task.id,
        })

    return render(request, 'upload_image.html')