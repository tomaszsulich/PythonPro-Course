# Zadanie 4 – Konfiguracja bazy danych

# Zmieniono domyślną konfigurację bazy danych z SQLite na PostgreSQL.
# Dane połączenia są przykładowe i służą wyłącznie do przećwiczenia konfiguracji.

# mojastrona/settings.py

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mojabaza",
        "USER": "postgres",
        "PASSWORD": "tajnehaslo123",
        "HOST": "localhost",
        "PORT": "5432",
    }
}