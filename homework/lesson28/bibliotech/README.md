# BiblioTech

Finalna wersja projektu na zakończenie modułu Django.

## Uruchomienie

```bash
python -m venv .venv

# Windows:
.venv\Scripts\activate

cd bibliotech

pip install -r requirements.txt

python manage.py migrate
python manage.py seed_db
python manage.py createsuperuser
python manage.py runserver
```

Testy:

```bash
python manage.py test --verbosity 2
```

Pełny plan projektu znajduje się w `docs/PROJECT_PLAN.md`.

Przy `--verbosity 2` każdy test jest wypisywany osobno wraz z wynikiem `ok`,
mimo że cały zestaw jest uruchamiany jednym poleceniem.


## Dane demonstracyjne

`python manage.py seed_db` tworzy przykładowy katalog książek, autorów, gatunków i egzemplarzy. Dla części książek próbuje również dobrać zdjęcia na podstawie motywu tytułu i zbudować z nich demonstracyjne okładki. Brak połączenia z Internetem nie przerywa seedowania.
