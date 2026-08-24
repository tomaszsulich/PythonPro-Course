# Plan integracji Celery z projektem Dice Tournament

## Planowany projekt

Dice Tournament to aplikacja webowa w Django służąca do organizowania i rozgrywania turniejów gry w kości. Projekt ma obsługiwać zarówno część organizacyjną turnieju, jak i samą rozgrywkę. W systemie przewidziane są
m.in. turnieje, etapy, rundy, grupy, gracze, stoły/mecze, rzuty oraz ranking.

Baza danych ma przechowywać pełną historię rozgrywki, a nie tylko końcowe wyniki. Każdy rzut ma być zapisany 
jako pełna migawka pięciu kości wraz z informacją o zatrzymanych kościach, wyborze kategorii, punktach 
i kolejności. Dzięki temu możliwe będzie późniejsze odtworzenie przebiegu gry.

Stoły w obrębie rundy mają działać niezależnie i nie czekać na siebie pomiędzy turami ani pojedynczymi rozgrywkami. Synchronizacja następuje przed wygenerowaniem kolejnej rundy grupowej, ponieważ jej skład 
może zależeć od wyników wszystkich stołów. Przed przejściem do fazy pucharowej wymagane jest zakończenie całego etapu.

Aplikacja ma wykorzystywać WebSockety do aktualizacji stołów i panelu organizatora w czasie rzeczywistym. WebSockety będą więc odpowiadały za komunikację w czasie rzeczywistym, natomiast Celery może zostać wykorzystany do zadań wykonywanych w tle.

## Zastosowanie Celery

Najbardziej naturalnym zastosowaniem Celery w projekcie jest obsługa zadań, które nie powinny blokować odpowiedzi HTTP ani działania interfejsu turnieju.

Pierwszym przykładem jest wysyłka wiadomości e-mail, np. podczas resetowania hasła w wariancie online. 
Django może przygotować dane potrzebne do resetu i zlecić wysłanie wiadomości do kolejki. Użytkownik otrzyma wtedy odpowiedź bez oczekiwania na komunikację z serwerem SMTP. W przypadku chwilowego błędu zadanie może zostać automatycznie ponowione.

Celery może być również wykorzystywany do operacji wykonywanych po poprawnym zapisaniu zmian w bazie. 
Przykładem może być dodatkowe przetwarzanie po zakończeniu turnieju albo przygotowanie danych do późniejszego porównania zakończonych turniejów. Takie zadania powinny otrzymywać wyłącznie identyfikatory obiektów, 
a nie całe obiekty Django.

Jeżeli zadanie zależy od danych zapisanych w ramach transakcji, powinno zostać wysłane do kolejki 
dopiero po jej zatwierdzeniu. Można to zapewnić przez `transaction.on_commit()`. Dzięki temu worker nie spróbuje pobrać obiektu, który nie jest jeszcze widoczny w bazie albo którego zapis zostanie później wycofany.

## Celery Beat

Celery Beat może zostać wykorzystany do zadań okresowych wymaganych przez architekturę projektu. 
Najbardziej naturalnym zastosowaniem są zadania utrzymaniowe wykonywane poza głównym przepływem gry, 
np. późniejsze czyszczenie lub anonimizacja danych po upływie ustalonego okresu przechowywania.

Dokładna polityka retencji danych nie jest jeszcze ostatecznie ustalona, dlatego nie traktowałbym konkretnego harmonogramu jako zamkniętego wymagania biznesowego. Celery Beat pozostaje jednak dobrym miejscem do realizacji tego typu okresowych operacji.

## Czego Celery nie powinien robić

Celery nie powinien odpowiadać za krytyczną logikę rozgrywki. Pierwszy rzut pięcioma kośćmi, zatrzymywanie kości, wybór kategorii, naliczanie punktów, zakończenie meczu oraz decyzja o przejściu do kolejnej rundy powinny pozostać w logice domenowej Django.

Nie przenosiłbym również do Celery komunikacji wymagającej natychmiastowej reakcji użytkownika. 
Aktualizacje stołów, panel organizatora oraz inne zdarzenia czasu rzeczywistego powinny pozostać po stronie ASGI i WebSocketów.

## Korzyści z integracji

Największą korzyścią z użycia Celery byłoby oddzielenie wolniejszych lub zależnych od usług zewnętrznych operacji od głównego procesu Django. Dzięki temu aplikacja mogłaby szybciej odpowiadać użytkownikowi, 
a problemy z pojedynczym zadaniem nie blokowałyby działania turnieju.

Kolejka umożliwia także ponawianie nieudanych zadań oraz późniejsze skalowanie liczby workerów niezależnie 
od serwera obsługującego stronę. W testach można osobno sprawdzać, czy kod poprawnie zleca zadanie 
przez `.delay()` z identyfikatorem, czy sam task wykonuje swoją funkcję oraz czy w przypadku błędu działa mechanizm `retry`.

## Podział odpowiedzialności

Django i serwisy domenowe odpowiadają za reguły gry, spójność danych i przejścia między etapami turnieju.

WebSockety odpowiadają za komunikację w czasie rzeczywistym pomiędzy stołami, uczestnikami i panelem organizatora.

Celery odpowiada za zadania wykonywane w tle, które mogą zostać wykonane chwilę później bez naruszenia spójności rozgrywki.

Celery Beat odpowiada za zadania okresowe.

## Wniosek

Integracja Celery z Dice Tournament przyniosłaby realne korzyści, ale powinna być selektywna. Celery najlepiej sprawdzi się przy wysyłce e-maili, zadaniach wykonywanych po zatwierdzeniu transakcji oraz operacjach okresowych realizowanych przez Celery Beat. Krytyczna logika turnieju i komunikacja w czasie rzeczywistym powinny pozostać poza kolejką zadań.
