# API Playground

Przykłady API omawiane podczas lesson16.

## Wymagane biblioteki

Serwer:

```bash
pip install fastapi uvicorn
```

Klient:

```bash
pip install requests
```

## Uruchomienie serwera

```bash
uvicorn server:app
```

lub w trybie automatycznego przeładowania po zmianach:

```bash
uvicorn server:app --reload
```

Gdzie:

- `server` oznacza nazwę modułu Python, czyli plik `server.py`
- `app` oznacza instancję klasy `FastAPI`

Opcja `--reload` jest przydatna podczas nauki i testowania, ponieważ serwer restartuje się automatycznie po zapisaniu zmian w pliku.

## Testowanie endpointów

Do obsługi plików `.http` w VS Code można użyć rozszerzenia **REST Client**.

Plik `requests.http` zawiera przykładowe żądania:

- `GET /cats`
- `POST /cats`
- `PATCH /cats/{cat_id}`

## Zawartość folderu

- `server.py` — serwer FastAPI z podstawowym CRUD dla kotów
- `cat_client.py` — prosty klient korzystający z biblioteki `requests`
- `cat_client_extended.py` — rozszerzony klient z obsługą kilku metod HTTP i błędów odpowiedzi
- `requests.http` — przykładowe żądania HTTP dla rozszerzenia REST Client
- `fake_server_api.py` — symulacja klient-serwer bez użycia FastAPI

## Uwaga

Ten folder ma charakter edukacyjny. Nie jest to pełna aplikacja produkcyjna, tylko przestrzeń do nauki działania API, metod HTTP, klienta, serwera i obsługi odpowiedzi.
