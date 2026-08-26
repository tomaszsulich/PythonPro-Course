# Zadanie 18 – Symulacja wyścigu w banku

## Parametry

Saldo początkowe: `200.37 zł`  
Liczba wątków wpłacających: `5`  
Liczba wątków wypłacających: `5`  
Zakres losowanych kwot: `10–100 zł`

## Przebieg

```text
Wypłacono: 91 zł
Wpłacono: 30 zł
Wpłacono: 53 zł
Wypłacono: 85 zł
Wypłacono: 52 zł
Odrzucono wypłatę: 81 zł
Wpłacono: 94 zł
Wpłacono: 76 zł
Wypłacono: 91 zł
Wpłacono: 86 zł
```

## Wynik

```text
Saldo początkowe: 200.37 zł
Saldo oczekiwane: 220.37 zł
Saldo końcowe: 220.37 zł
Weryfikacja: True
```

## Notatka

Saldo może zawierać grosze, natomiast symulowane wpłaty i wypłaty dotyczą
pełnych kwot w złotych.

Kolejność operacji jest losowana przed uruchomieniem wątków, aby nie wymuszać
naprzemiennego schematu wpłata–wypłata.

Dostęp do salda jest chroniony blokadą. Sprawdzenie dostępnych środków
i wykonanie wypłaty odbywają się w tej samej sekcji krytycznej.

Reprezentatywny przebieg zawiera zarówno udane operacje, jak i odrzuconą
wypłatę z powodu niewystarczających środków.

Program został dodatkowo uruchomiony 500 razy w ramach stress testu.
Wszystkie 500 wykonań zakończyło się poprawną weryfikacją salda.
