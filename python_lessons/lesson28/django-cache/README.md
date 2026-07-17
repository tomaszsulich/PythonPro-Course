# Django Cache

## Stack

- Python
- Django
- Django REST Framework
- JWT Authentication
- Redis
- Docker
- drf-spectacular (Swagger / OpenAPI)

## Uruchomienie

1. Sklonuj repozytorium.
2. Uruchom Redis:

```bash
docker compose up -d
```

3. Wykonaj migracje:

```bash
python manage.py migrate
```

4. (Opcjonalnie) utwórz administratora:

```bash
python manage.py createsuperuser
```

5. Uruchom serwer:

```bash
python manage.py runserver
```

## Przykładowe dane

Repozytorium zawiera własne polecenie umożliwiające wygenerowanie przykładowych danych biznesowych:

```bash
python manage.py seed_data
```

Aby usunąć dotychczasowe dane i wygenerować je ponownie:

```bash
python manage.py seed_data --clear
```

Polecenie nie tworzy użytkowników Django. Konta użytkowników należy utworzyć samodzielnie (np. przez endpoint rejestracji lub panel administracyjny).

## Dokumentacja

Informacje dotyczące rekonstrukcji brakujących elementów projektu oraz autorskich rozszerzeń znajdują się w pliku `NOTES.md`.