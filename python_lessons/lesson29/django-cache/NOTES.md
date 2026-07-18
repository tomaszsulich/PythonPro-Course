## Rekonstrukcja projektu
Nagranie z tej lekcji rozpoczyna się już z istniejącym projektem, dlatego część kodu należało odtworzyć samodzielnie.

## Modele
Podczas zajęć prowadzący pokazał jedynie fragment pliku `shop/models.py`, obejmujący modele:

- `Address`
- `Client`
- `Category`
- `Product`

Widoczny fragment został odtworzony zgodnie z materiałem wideo.

Pozostałe modele (`Transaction` oraz `TransactionItem`) nie były ponownie omawiane podczas zajęć, dlatego pozostawiono ich implementację zgodną z poprzednią lekcją.

## Pozostałe elementy projektu
Pozostałe elementy projektu (m.in. serializery, widoki oraz routing) zostały zachowane lub odtworzone na podstawie poprzedniej lekcji, ponieważ prowadzący nie prezentował ich ponownie.

## Dokumentacja API
Podczas zajęć skonfigurowano automatyczne generowanie dokumentacji API z wykorzystaniem biblioteki **drf-spectacular**.

Omówiono między innymi:

- generowanie schematu OpenAPI,
- Swagger UI,
- wykorzystanie docstringów,
- opisy parametrów endpointów,
- definiowanie kodów odpowiedzi.

## Folder `django-cache`
Folder `django-cache` był widoczny w strukturze projektu podczas zajęć, jednak jego zawartość nie została pokazana.

Z tego powodu pozostawiono go pustego (z plikiem `.gitkeep`, umożliwiającym śledzenie katalogu przez Git).