# projekt/articles/models/category.py
from django.db import models as m
# pod komentarzem ze ścieżką do danego pliku wypisujemy kod, jaki umieszczamy w tym pliku


# le22\le22\settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"], # <- tu możemy dodać info, że zmodyfikowane
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# wszystkie zmiany związane z jednym zadaniem możemy robić w powyższy sposób