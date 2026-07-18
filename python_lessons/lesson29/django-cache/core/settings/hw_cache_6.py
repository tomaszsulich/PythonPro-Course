import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'django_cache'),
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}