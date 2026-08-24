import csv
import random
import time
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup
from celery import shared_task
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

from .models import EmailNotification, LogEntry, ScrapedPage, UploadedImage


# Używamy dekoratora @shared_task, aby zadanie było dostępne
# w całej aplikacji, bez potrzeby bezpośredniego importowania instancji Celery.
@shared_task
def add(x: float | int, y: float | int) -> float | int:
    """Proste zadanie, które dodaje dwie liczby."""
    return x + y


@shared_task
def classify_image(image_id: int) -> None:
    """Analizuje właściwości obrazu i zapisuje wyniki klasyfikacji."""
    uploaded_image = UploadedImage.objects.get(pk=image_id)

    with Image.open(uploaded_image.image.path) as image:
        width, height = image.size
        image_format = image.format or 'nieznany'
        image_mode = image.mode

        rgb_image = image.convert('RGB')

        is_grayscale = all(
            red == green == blue
            for red, green, blue in rgb_image.getdata()
        )

        if is_grayscale:
            image_type = 'skala szarości'
        else:
            image_type = 'kolorowy'

        if width > height:
            orientation = 'poziomy'
        elif width < height:
            orientation = 'pionowy'
        else:
            orientation = 'kwadratowy'

        pixel_count = width * height
        has_alpha = 'A' in image.getbands()

    uploaded_image.image_type = image_type
    uploaded_image.image_format = image_format
    uploaded_image.image_mode = image_mode
    uploaded_image.width = width
    uploaded_image.height = height
    uploaded_image.orientation = orientation
    uploaded_image.pixel_count = pixel_count
    uploaded_image.has_alpha = has_alpha

    uploaded_image.classification_result = (
        f"Obraz {image_type}, {orientation}, {width}×{height} px."
    )

    uploaded_image.save(
        update_fields=[
            'image_type',
            'image_format',
            'image_mode',
            'width',
            'height',
            'orientation',
            'pixel_count',
            'has_alpha',
            'classification_result',
        ]
    )


@shared_task
def cleanup_old_logs() -> None:
    print("Rozpoczynam czyszczenie starych logów...")
    cutoff_date = timezone.now() - timedelta(days=90)
    LogEntry.objects.filter(created_at__lt=cutoff_date).delete()
    print("Logi wyczyszczone.")


@shared_task
def count_users() -> None:
    user_count = User.objects.count()
    print(f"Liczba użytkowników: {user_count}.")


@shared_task
def generate_random_number() -> int:
    return random.randint(1, 100)


@shared_task
def generate_users_csv() -> str:
    reports_dir = settings.MEDIA_ROOT / 'reports'
    reports_dir.mkdir(parents=True, exist_ok=True)

    timestamp = timezone.localtime().strftime('%Y-%m-%d_at_%H-%M-%S')
    filename = f'users_report_{timestamp}.csv'
    file_path = reports_dir / filename

    with file_path.open('w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['username', 'email'])

        for user in User.objects.all():
            writer.writerow([user.username, user.email])

    return f'reports/{filename}'


@shared_task
def hello_world() -> None:
    print("Hello from Celery!")


@shared_task
def log_timestamp() -> None:
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f"{datetime.now()}\n")


@shared_task
def multiply(a: float | int, b: float | int) -> float | int:
    return a * b


@shared_task
def multiply_by_ten(number: int) -> int:
    return number * 10


@shared_task
def process_video() -> None:
    time.sleep(15)


@shared_task(bind=True)
def retry_failed_request(self) -> None:
    url = 'https://this-page-does-not-exist.invalid'

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as exc:
        print(
            f"Nie udało się połączyć z {url}. "
            "Ponawiam próbę za 60 sekund."
        )

        raise self.retry(
            exc=exc,
            countdown=60,
            max_retries=3,
        )


@shared_task
def save_result_to_file(result: int) -> str:
    results_dir = settings.MEDIA_ROOT / 'chain_results'
    results_dir.mkdir(parents=True, exist_ok=True)

    timestamp = timezone.localtime().strftime('%Y-%m-%d_at_%H-%M-%S')
    filename = f'chain_result_{timestamp}.txt'
    file_path = results_dir / filename

    file_path.write_text(
        f"Wynik łańcucha: {result}",
        encoding='utf-8',
    )

    return f'chain_results/{filename}'


@shared_task
def scrape_page_title() -> None:
    url = 'https://example.com'

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string

    ScrapedPage.objects.create(
        url=url,
        title=title,
    )


@shared_task
def send_email_notification(notification_id: int) -> None:
    notification = EmailNotification.objects.get(pk=notification_id)

    print(
        f"Wysyłanie maila do {notification.recipient_email}: "
        f"{notification.subject}"
    )

    time.sleep(10)

    notification.sent_at = timezone.now()
    notification.save(update_fields=['sent_at'])
    print(f"Mail do {notification.recipient_email} wysłany.")


@shared_task
def send_periodic_summary(user_emails: list[str]) -> None:
    print(f"Wysyłanie podsumowania do {len(user_emails)} użytkowników...")
    # Tutaj logika wysyłania maili
    print("Podsumowanie wysłane.")


@shared_task
def send_priority_email(recipient_email: str) -> None:
    print(f"Wysyłanie priorytetowego maila do {recipient_email}...")
    time.sleep(5)
    print(f"Mail do {recipient_email} wysłany.")


@shared_task
def send_welcome_email(user_email: str) -> bool:
    """
    Symuluje wysyłanie maila powitalnego.
    W rzeczywistej aplikacji tutaj znalazłby się kod do wysyłki maila.
    """
    print(f"Wysyłanie maila powitalnego do {user_email}...")
    time.sleep(10)  # Symulacja opóźnienia związanego z serwerem SMTP
    print(f"Mail do {user_email} wysłany.")
    return True


@shared_task
def simulate_cpu_bound_task(duration: float | int) -> str:
    """
    Symuluje długotrwałe zadanie CPU-bound, np. generowanie raportu.
    Używamy time.sleep(), aby zasymulować opóźnienie.
    """
    print(f"Rozpoczynam zadanie, które potrwa {duration} sekund...")
    time.sleep(duration)
    print("Zadanie zakończone.")
    return f"Raport wygenerowany pomyślnie po {duration} sekundach."


@shared_task(bind=True)
def track_progress(self) -> str:
    """Aktualizuje stan zadania Celery podczas wykonywania kolejnych iteracji."""
    for i in range(1, 101):
        time.sleep(0.1)

        self.update_state(
            state='PROGRESS',
            meta={
                'current': i,
                'total': 100,
            },
        )

    return "Zadanie zakończone."


@shared_task
def update_user_last_login(user_id: int) -> None:
    user = User.objects.get(pk=user_id)
    user.last_login = timezone.now()
    user.save(update_fields=['last_login'])