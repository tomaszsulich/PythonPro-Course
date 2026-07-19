import os
from celery import Celery

# Ustawienie domyślnego modułu ustawień Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Pobieranie konfiguracji z settings.py (z prefiksem CELERY_)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatyczne wykrywanie zadań w plikach tasks.py we wszystkich aplikacjach
app.autodiscover_tasks()