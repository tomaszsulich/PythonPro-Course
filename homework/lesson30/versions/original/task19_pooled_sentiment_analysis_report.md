# Zadanie 19 – AI: Równoległa analiza sentymentu (symulacja)

## Parametry

Liczba opinii: `20`  
Liczba wątków w puli: `5`  
Symulowane opóźnienie API: `0.5–2.0 s`

## Wyniki analizy

```text
Pozytywny: Produkt działa dokładnie tak, jak oczekiwałem.
Negatywny: Jakość wykonania jest bardzo dobra.
Negatywny: Przesyłka dotarła znacznie później niż powinna.
Negatywny: Obsługa klienta szybko rozwiązała mój problem.
Negatywny: Produkt przestał działać po kilku dniach.
Negatywny: Cena jest adekwatna do jakości.
Negatywny: Opakowanie było uszkodzone.
Pozytywny: Produkt jest łatwy w obsłudze.
Neutralny: Nie zauważyłem żadnej szczególnej różnicy.
Neutralny: Jestem bardzo zadowolony z zakupu.
Negatywny: Instrukcja mogłaby być bardziej czytelna.
Pozytywny: Produkt spełnia podstawowe wymagania.
Negatywny: Kolor wygląda inaczej niż na zdjęciach.
Negatywny: Dostawa przebiegła szybko i bez problemów.
Neutralny: Nie kupiłbym tego produktu ponownie.
Pozytywny: Wszystko działa poprawnie.
Pozytywny: Produkt jest przeciętny, ale spełnia swoje zadanie.
Negatywny: Materiały wydają się solidne.
Neutralny: Cena jest zdecydowanie za wysoka.
Pozytywny: Zakup okazał się dobrym wyborem.
```

## Czas wykonania

```text
Czas wykonania: 5.81 s
```

## Notatka

Analiza sentymentu jest symulowana zgodnie z treścią zadania. Opóźnienie imituje czas odpowiedzi API AI, natomiast wynik sentymentu jest wybierany losowo i nie wynika z rzeczywistej analizy znaczenia opinii.

Do przetwarzania 20 opinii wykorzystano pulę pięciu wątków `ThreadPoolExecutor`. Dzięki temu symulowane oczekiwanie na odpowiedzi API może odbywać się współbieżnie.

Wyniki są zwracane w kolejności odpowiadającej kolejności opinii wejściowych.

Pomiar czasu obejmuje analizę wszystkich 20 opinii.
