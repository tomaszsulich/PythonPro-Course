INSTALLED_APPS = [
    # ... inne aplikacje ...
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware', # Najlepiej na początku (ale po GZip, jeśli używasz)
    # ... inne middleware ...
]

# Adresy IP, dla których toolbar ma być widoczny
INTERNAL_IPS = [
    "127.0.0.1",
]