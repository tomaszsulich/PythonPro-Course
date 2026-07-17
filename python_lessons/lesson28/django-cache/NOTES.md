Projekt został uzupełniony na podstawie materiałów z lesson27 oraz struktury projektu widocznej podczas lesson28.

Ponieważ prowadzący rozpoczął lekcję od wcześniej przygotowanego rozwiązania pracy domowej, odtworzono następujące elementy:

- `shop/models.py`
- `shop/serializers.py`
- `shop/urls.py`

Ich implementacja została przygotowana na podstawie kodu z lesson27 oraz zależności widocznych w `shop/views.py`.

Podczas lekcji widoczny był również folder `shop/management`, jednak jego zawartość nie została pokazana. Nie było więc możliwe odtworzenie jego oryginalnej implementacji na podstawie nagrania.

Dla wygodnego zasilania bazy przykładowymi danymi dodano własne polecenie:

- `shop/management/commands/seed_data.py`

Polecenie generuje dane dla modeli:

- `Address`
- `Client`
- `Category`
- `Product`
- `Transaction`
- `TransactionItem`

Implementacja `seed_data.py` nie pochodzi z materiału kursowego. Została dodana jako własne narzędzie pomocnicze, aby projekt był kompletny i łatwiejszy do uruchamiania oraz testowania.

Polecenie nie tworzy ani nie usuwa użytkowników Django. Użytkownik testowy jest rejestrowany osobno przez endpoint:

```http
POST /auth/users/