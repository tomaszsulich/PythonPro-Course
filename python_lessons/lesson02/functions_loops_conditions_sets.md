## funkcje

Funkcja - wydzielony blok kodu, który realizuje konkretne zadanie i może być wielokrotnie używany w różnych miejscach programu. Pozwala to ograniczyć powtarzanie kodu, poprawia czytelność oraz ułatwia testowanie i modyfikacje.

```python
def nazwa_funkcji(arg0, arg1):
    # kod/ciało funkcji
    return result
```
Powyżej prosty przykład funkcji:<br>
- `def` - kluczowa instrukcja mówiaca pythonowi, że zaczynamy definicje funkcji <br>
- `nazwa_funkcji` - identyfikator, po którym będziemy się do niej odwoływać. zwyczajowo w python nazywamy funkcje "snake_casem" tj. małe litery, słowa oddzielone `_`, a nazwa funkcji powinna być poleceniem mówiącym, co ona robi. (np. `get_user`, `search_video`, `find_title`, `filter` itd.)
- `return` - czyli to, co funkcja ma zwrócić. Nie jest ona obowiązkowa, bo funkcja nie zawsze musi cos zwrócić.
Przykładem funkcji, która nic nie zwraca może być `print`, który wypisuje rzeczy do konsoli i koniec.

Funkcje wywołujemy poprzez jej nazwę z dodanymi nawiasami, w których podajemy argumenty funkcji.
```python
nazwa_funkcji(10, 11)
```

Poniższa funkcja potęguje wartość argumentu:
```python
def power(x):
    return x*x
```
A poniższa funkcja wypisuje jedynie tekst do konsoli, nic nie zwraca.
```python
def say_hello():
    print('Hello world!')
```

### Czy funkcja rzeczywiście może nic nie zwracać?
Na poniższym przykładzie widzimy, że pomimo braku użyciu polecenia `return`, w wyniku dostajemy jakieś `None`.
```python
>>> def say_hello():
...     print('Hello world!')
... 
>>> result = say_hello()
Hello world!
>>> print(result)
None
```
`None` jest pythonowym "brakiem wartości", bytem który mówi, że nic tu nie ma (pomimo, że jest). Python, jeżeli nie znajdzie returna, dodaje automatycznie `return None` na końcu.

### Domyślne wartosci argumentów

argumenty naszej funkcji mogą mieć wartości domyślne, np. poniższa funkcja potęguje (`**`) wartość argumentu `base` do potęgi `exp`.

```python
def power(base, exp=2):
    return base ** exp

power(2)
>>> 4
power(2, 10)
>>> 1024
```
z racji tego, że przypisaliśmy argumentowi `exp` wartość `2`, to w przypadku, kiedy nie podamy innej, funkcja domyślnie używa właśnie tej wartości.

### args vs kwargs
Argumenty możemy przekazywać **pozycyjnie** lub poprzez słowa kluczowe (tzw. `kwargs`):
```python
power(2, exp=10)
```
`Pozycyjnie` - czyli podajemy wartosci oddzielone przecinkiem, a program przypisuje je po kolei do kolejnych parametrów. (przykład z 2 - zwyczajnie przekazana jest przypisana do pierwszego argumentu)<br>
`słowa klucze` - instrukcją `nazwa_parametru=jego_wartosc` (przykład z exp=10).

[!warning]
>możemy używać ich na raz (jak w powyższym przykładzie), ale po pierwszym przypisaniu przez klucz, kolejne wartości musimy przekazywać w ten sam sposób, inaczej python wyrzuci błąd.


### Opis funkcji
Nasza funkcja może zawierać również opis.
- `: <type>` dodany po argumencie jest informacją dla użytkownika, jakiej wartości oczekujemy, że tutaj dostaniemy.
- `-> <type>` po jest informacją, jakiego typu wartość zostanie zwrócona. 
- `"""<docsting>"""` pod nazwą funkcji to tak zwany `docstring` (string-dokumentacja), w którym możemy opisać działanie funkcji. Przydatne, kiedy piszemy kod dla kogoś lub kodu mamy dużo.

```python
def power(base: float, exp: int = 2)-> float:
    """Returns base to the power of exp"""
    return base ** exp
```

>[!warning]
> nazywając dowolną zmienną, funkcje, klasę uważaj, aby nie nadpisać czegoś wbudowanego w python, gdyż ten jezyk na to pozwala. Przykładowo nazywając coś `print` nadpisujemy wbudowanego `print'a` i od tej pory to nasza funkcja będzie zamiast niego używana w tym konkretnym kodzie!



## Instrukcje warunkowe

Celem instrukcji warunkowych jest wykonanie jakiejś akcji/kodu w zależności od zadanego warunku.

### if, elif, else

Najprostszym warunkiem w python jest pojedyncza instrukcja `if`.
```python
if some_condition:
    # do something
```
np.
```python
predkosc_pojazdu = zmierz_predkosc()
if predkosc_pojazdu >= 60:
    zatrzymaj_pojazd()
    daj_mandat(200)
```
Warunki możemy ze sobą kojarzyć przy użyciu `elif` (w przeciwnym wypadku, jeżeli ...) i `else` (domyślna opcja, jeżeli żaden warunek nie został spełniony). <br>

```python
predkosc_pojazdu = zmierz_predkosc()
if predkosc_pojazdu >= 100:
    zatrzymaj_pojazd_do_kontroli()
    daj_mandat(1000, punkty=20)
elif predkosc_pojazdu>=70:
    zatrzymaj_pojazd_do_kontroli()
    daj_mandat(500, 15)
elif predkosc_pojazdu>50:
    zatrzymaj_pojazd_do_kontroli()
    daj_mandat(pln=200, punkty=10)
else:
    pozdrow()
```
`elif` oraz `else` są nieobowiązkowe i możemy używać ich niezależnie. Kluczowe jest, aby przed nimi stał `if`.

- warunki sprawdzane są po kolei i wykona się ten, który pierwszy zostanie spełniony,
- jeżeli żaden nie zostaje spełniony, wykona się instrukcja `else` (o ile ją dodamy),
- ilość `elif` może być dowolna.

Przy warunkach korzystamy z instrukcji `or` i `and`, które są działaniami podobnymi do `*`, `-` itd. ale zwracają wartości typu `bool` (Czyli `True` albo `False`)

`x or y` - wystarczy, że `x` lub `y` będzie prawdziwe, a `or` zwróci `True`.<br>
`x and y` - wymaga, aby `x` i `y` były prawdziwe.<br>
<br>

```python
predkosc_pojazdu = zmierz_predkosc()
czy_swiatla_wylaczone = sprawdz_czy_swiatla_wylaczone()
if predkosc_pojazdu >= 100:
    zatrzymaj_pojazd_do_kontroli()
    daj_mandat(1000, punkty=20)
elif 100>predkosc_pojazdu and predkosc_pojazdu>=70:
    zatrzymaj_pojazd_do_kontroli()
    daj_mandat(500, 15)
elif predkosc_pojazdu > 50 and czy_swiatla_wylaczone:
    zatrzymaj_pojazd_do_kontroli()
    daj_mandat(pln=200, punkty=10)
else:
    pozdrow()
```

Warunki można łączyć i będą one sprawdzane od lewa do prawa.
```python
if pw or dw and tw:
```
Python traktuje `and` priorytetowo i względem `or` dlatego nie zawsze będą one wykonywane po kolei. W powyższym przykładzie pierwsze wykona się `dw and tw` a dopiero później `pw or wynik_anda`.

```python
a = True
b = False
c = True

if a or b and c:  # równoważne if a or (b and c)
    print("Wykona się, bo a jest True")
```

<br>
Kolejnością można manipulować przy pomocy nawiasów.

```python
if (a or b) and c:
    print("Teraz warunek zależy od obu części")
```

W przypadku długich warunków możemy warunki wyliczyć przed instrukcją warunkową.
```python
czy_wykonac = warunek1 or warunek2 and x>10
if czy_wykonac:
    ...
```
>[!warning]
> W przypadku, gdy chcemy sprawdzić, czy jakaś wartość jest `True`, `False` albo `None` używamy operatora `is` zamiast `==`. (`x is True`) gdyż są to "specyficzne" wartości.

W warunkach często korzysta się z instrukcji `not` która jest zaprzeczeniem. Odwraca ona nasz warunek, np. `not True` będzie traktowane jak `False`.

```python
if not True:
    # nie wykona się
if not 0 > 10: 
    # wykona się
```



Instrukcje warunkowe możemy zagnieżdżać, ale staramy się tego unikać z powodu czytelności kodu.
```python
if condition0:
    if condition1:
        # do something
        if othercondition:
            ...
        elif condition4:
            ...
    else:
        # do something else
elif condition2:
    ...
```

### Dodatkowo warto wiedzieć

Python niektóre wartości z góry interpretuje jako fałsz, i są to zmienne z domyślnymi wartości, np:
- `0.0` (float)
- `0` (int)
- `[]` (pusta lista),
- `{}` (pusty słownik),
- `None`,
- `False`,
- `""` (pusty str) 

Zaś jeżeli dodamy do zbioru jakiś element, string będzie miał min 1 znak lub liczby będzą != 0, wtedy będą traktowane jako `True`.

- `x > y and y > z` jest równoważne do `x > y > z`.

## Zbiory danych

W Pythonie mamy kilka podstawowych typów przechowujących dane.

### Lista (list)

Uporządkowana kolekcja elementów.
```python
lista = [1, 2, 3]
```

Cechy:
- zachowuje kolejność
- można zmieniać (mutable)
- pozwala na duplikaty

Dostęp do elementu:
```python
lista[0]
```

Dodawanie:
```python
lista.append(4)
```
Listy można łączyć
```python
[1, 2, 3] + [4, 5, 6]
>>> [1, 2, 3, 4, 5, 6]
```

### in
`in` służy do sprawdzenia, czy dana wartość znajduje się z liście
```python
1 in [1, 2, 3]
>>> True
-1 in [1, 2, 3]
>>> False
```

### slicing
Czyli służy do wydzielenia podlisty.

```python
# lista[start:koniec:krok] <- schemat

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[:4] # 4 pierwsze elementy
>>>[1, 2, 3, 4]
a[2:] #pomija 2 pierwsze elementy
>>> [3, 4, 5, 6, 7, 8, 9]
a[::2] #co drugi element
>>[1, 3, 5, 7, 9]
a[2:6:2] 
>>[3, 5]
```

Slicing przyjmuje też ujemne wartości, które liczą index od końca:
```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst[-5:] #5 ostatnich elementów
>>>[5, 6, 7, 8, 9]
```

String w dużej mierze jest traktowany jako lista i większość operacji, które wykonujemy na liście, możemy wykonać również na nim.


### Krotka (tuple)

Podobna do listy, ale niemodyfikowalna.
```python
krotka = (1, 2, 3)
```

Cechy:
- nie można jej modyfikować. każda zmiana wymaga stworzenia nowej krotki (jest immutable)
- szybsza niż lista
- używana do stałych danych
  
### Słownik (dict)
Przechowuje dane w postaci klucz-wartość.
```python
slownik = {
    "imie": "Jan",
    "wiek": 30}
```

Dostęp:
```python
# w przypadku braku klucza wyrzuci błąd i przerwie program
slownik["imie"]
```
lub
```python
#w przypadku braku klucza zwróci None, lub wartosc podana jako drugi argument
slownik.get("imie") 
```

Dodawanie / zmiana:
```python
slownik["wiek"] = 31
```
`in` w przypadku słówników sprawdza klucze, nie wartości.
```python
slownik = {
    "imie": "Jan",
    "wiek": 30}
'imie' in slownik
>> True
"Jan" in slownik
>> False
```

### Zbiór (set)

Nieuporządkowana kolekcja unikalnych elementów.
```python
zbior = {1, 2, 3}
```
Cechy:
-brak duplikatów
-brak indeksowania

Dodawanie:
```python
zbior.add(4)
```
Operacje na zbiorach (set)
```python
a = {1, 2, 3}
b = {3, 4, 5}

a & b  # część wspólna
a | b  # suma
a - b  # różnica
```

Podsumowanie zbiorów w python:
lista – najczęściej używana, zmienna <br>
krotka – stała <br>
słownik – klucz-wartość<br>
zbiór – unikalne elementy<br>

Przydatną funkcją przy zbiorach jest `len`, która zwraca ilość elementów zbioru.
```python
len([1,2,3,4])
>>>4
```

Zbiory można dowolnie zagnieżdżać i nic nie stoi na przeszkodzie, aby stworzyć listę list, listę słowników itd.
```python
lst = [
    {'a':1, 'b':2, 'c':3},
    {'a':8, 'b':4, 'c':1}]

dct = {
    'a': [1, 2, 3, 4, 5],
    'b': [6, 7, 8, 9, 10]}
```


## Pętle

Pętle służą do wielokrotnego wykonywania tego samego fragmentu kodu. Zamiast powtarzać ten sam kod ręcznie, używamy pętli.

### Pętla for

Pętla for służy do iterowania po zbiorach danych (np. listach, stringach, zakresach).

Ogólna składnia:

for element in kolekcja:
    # kod wykonywany dla każdego elementu

Przykład:
```python
for i in range(5):
    print(i)
```
Wynik:
```
0
1
2
3
4
```

Funkcja `range(n)` generuje liczby od 0 do n-1 i jest ona używana jako domyślna, kiedy chcemy iterować n razy.

Możemy też iterować po liście:
```python
liczby = [10, 20, 30]

for liczba in liczby:
    print(liczba)
```
Po każdym przebiegu pętli zmienna (liczba) przyjmuje kolejną wartość ze zbioru.

### Pętla while

Pętla while wykonuje się tak długo, jak długo warunek jest prawdziwy.

Składnia:
```python
while warunek:
    # kod
```
Przykład:
```python
i = 0

while i < 5:
    print(i)
    i += 1
```
Ważne:

trzeba pilnować zmiany warunku
inaczej powstanie pętla nieskończona

### break i continue

`break` – przerywa pętlę całkowicie
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```
`continue` – pomija aktualną iterację
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
else w pętlach
```
Pętle mogą mieć blok else, który wykona się, jeśli pętla zakończy się normalnie (bez break)
```python
for i in range(3):
    print(i)
else:
    print("koniec")
```
### enumerate

Jeśli potrzebujemy indeksu i wartości:
```python
lista = ["a", "b", "c"]

for i, val in enumerate(lista):
    print(i, val)
```
Podsumowanie pętli
`for` – gdy iterujemy po zbiorze
`while` – gdy mamy warunek
`break` – przerywa pętlę
`continue` – pomija iterację




## ZADANIA

### zad 1
Przeiteruj po liscie `temps` i jeżeli temp jest >=20 wypisz(`print`) `warm` a jeżeli <=10 `cold`, a dla pozostałych `med_warm`.
temps = [12, 15, 14, 18, 20, 19, 24, 21, 18, 17, 24]

Podpowiedzi:
- użyj petli `for` 
- instrukcji warunkowej `if`,`elif`, `else`.

### zad 2
Napisz funkcje `desc_temp`, która będzie opisywać temp. zgodnie z warunkami z zad 1.
Funkcja ma przyjmować wartosc liczbową, a **zwrcać** stringa.

Następnie użyj jest zamiast instrukcji warunkowej z pierwszego zadania w identycznej pętli.

Podpowiedzi:
- użyj `return` zamiast `print`
  

### zad 3
połącz listę temps i `rains` (poniżej) 
`rains = [False, False, True, False, True, False, False, True, True, False, False]`
w listę słowników `weather_data`, która ma wygladać następująco:
```python
weather_data = [{'temp': ..., 'rain': ...},
                {'temp': ..., 'rain': ...}]
```

### zad 4
Napisz funkcja `is_nice_weather`, która:
- Funkcja przyjmuje dwa argumenty: temp(int) i rain(bool) oraz zwraca bool
- Uzna dzień za „ładny” (i zwróci True), jeśli temperatura jest >= 15 i <= 25 i nie pada.
- uzna dzień za brzydki (i zwróci False), dla innych warunków pogodowych.
Następnie iteruj po liście weather_data i przy pomocy tej funkcji zlicz ilość ładnych dni.

Podpowiedzi:
- zliczyć elementy możesz przy pomocy dodatkowe licznika lub przypisując 
- lub przypisując wyniki do listy a następnie policzyć ilość występujących w niej wartości True.

Przykładowo lista, jeżeli nie użyjesz tej z zad 3.
```python
weather_data = [
    {'temp': 12, 'rain': False},
    {'temp': 15, 'rain': False},
    {'temp': 14, 'rain': True},
    {'temp': 18, 'rain': False},
    {'temp': 20, 'rain': True},
    {'temp': 19, 'rain': False},
    {'temp': 24, 'rain': False},
    {'temp': 21, 'rain': True},
    {'temp': 18, 'rain': True},
    {'temp': 17, 'rain': False},
    {'temp': 24, 'rain': False},
]
```

