# Django Cache

Projekt demonstracyjny przedstawiający wybrane zagadnienia związane z Django REST Framework.

## Zakres projektu

Projekt prezentuje między innymi:

- cache widoków (`cache_page`)
- różny czas przechowywania danych w cache
- dokumentację API z wykorzystaniem Swagger UI
- generowanie specyfikacji OpenAPI przy użyciu `drf-spectacular`
- podstawową konfigurację Django REST Framework

## Uruchomienie

```bash
python manage.py migrate
python manage.py runserver
```

Po uruchomieniu aplikacji dokumentacja API dostępna jest pod skonfigurowanymi adresami Swagger UI oraz schematu OpenAPI.

## Uwagi

Informacje dotyczące rekonstrukcji projektu oraz autorskich uzupełnień znajdują się w pliku `NOTES.md`.