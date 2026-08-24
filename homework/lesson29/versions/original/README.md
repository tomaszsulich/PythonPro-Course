# Uwagi

## Zadanie 19 - Flower

W używanej wersji Flower 2.1.0 interfejs webowy umożliwia monitorowanie zadań oraz zarządzanie workerami,
ale nie udostępnia opcji ręcznego wykonania zadań.

Zadania można uruchamiać programowo lub za pośrednictwem API Flower, natomiast ich wykonanie i stan są widoczne w zakładce Tasks.

## Zadanie 20 - Transakcje bazodanowe i zadania Celery

Zadanie Celery powinno zostać wysłane do kolejki dopiero po pomyślnym zatwierdzeniu transakcji. 
W przeciwnym razie worker może próbować pobrać obiekt, który nie jest jeszcze widoczny w bazie lub którego zapis zostanie później wycofany.

`transaction.on_commit()` pozwala zarejestrować callback wykonywany dopiero po poprawnym zatwierdzeniu transakcji.
Jeśli transakcja zostanie wycofana, zadanie Celery nie zostanie wysłane.