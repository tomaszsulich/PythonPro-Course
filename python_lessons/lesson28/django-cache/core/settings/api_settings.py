from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':
    ('rest_framework_simplejwt.authentication.JWTAuthentication', ),
    'DEFAULT_SCHEMA_CLASS':
    'drf_spectacular.openapi.AutoSchema'
}

SIMPLE_JWT = {
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ACCESS_TOKEN_LIFETIME": timedelta(seconds=10)
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Moje Wspaniałe API Projektu',
    'DESCRIPTION': 'Dokumentacja dla API, które robi niesamowite rzeczy.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA':
    False, # Zazwyczaj nie chcemy udostępniać pliku schematu publicznie
}