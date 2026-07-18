# cache lokalny w pamięci
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-cache", # Nazwa uniknalna dla instancji
    }
}