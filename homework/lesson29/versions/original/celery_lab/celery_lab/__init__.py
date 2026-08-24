# Importujemy naszą aplikację Celery, aby była dostępna przy starcie Django
from .celery import app as celery_app

__all__ = ('celery_app',)