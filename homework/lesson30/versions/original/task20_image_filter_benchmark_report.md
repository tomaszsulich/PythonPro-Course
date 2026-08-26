# Zadanie 20 – AI: Równoległe przetwarzanie obrazów (symulacja)

## Parametry

Liczba obrazów: `10`  
Rozmiar obrazu: `1000 × 1000`  
Liczba prób: `7`  
Zakres wartości pikseli: `0–255`  
Operacja na pikselu: `piksel * 1.1`

## Faza 1 – Benchmark bazowy

### Pomiary

| Próba | Sekwencyjnie | Równolegle | Przyspieszenie |
| ---: | ---: | ---: | ---: |
| 1 | 0,467 s | 19,205 s | 0,024× |
| 2 | 0,481 s | 16,979 s | 0,028× |
| 3 | 0,419 s | 16,505 s | 0,025× |
| 4 | 0,402 s | 18,211 s | 0,022× |
| 5 | 0,441 s | 13,161 s | 0,034× |
| 6 | 0,388 s | 13,410 s | 0,029× |
| 7 | 0,658 s | 14,802 s | 0,044× |

### Statystyki

| Miara | Sekwencyjnie | Równolegle |
| --- | ---: | ---: |
| Średnia | 0,465 s | 16,039 s |
| Mediana | 0,441 s | 16,505 s |
| Odchylenie standardowe | 0,085 s | 2,157 s |
| Rozstęp | 0,270 s | 6,044 s |

### Porównanie

Przyspieszenie według średnich czasów: `0,029×`

Przyspieszenie według median czasów: `0,027×`

### Analiza

We wszystkich próbach wykonanie sekwencyjne było wyraźnie szybsze od równoległego. Dla badanego przypadku narzut związany z wykorzystaniem wielu procesów przewyższa korzyść wynikającą z równoległego wykonywania prostej operacji na pikselach.

Jedną z możliwych przyczyn jest niewielki koszt pojedynczej operacji `piksel * 1.1` w porównaniu z kosztami uruchamiania procesów, serializacji danych i ich przekazywania między procesami.

Wykonanie równoległe wykazało również większy bezwzględny rozrzut czasów w przeprowadzonych próbach.

Faza 1 stanowi punkt odniesienia do sprawdzenia, czy zwiększenie kosztu obliczeniowego przypadającego na pojedynczy piksel może doprowadzić do sytuacji, w której wieloprocesowość zacznie przynosić korzyść.

**Uwaga:** po zakończeniu Fazy 1 program rozszerzono o możliwość regulowania kosztu obliczeniowego przez wielokrotne wykonywanie operacji na każdym pikselu. Wartość `1` w finalnej wersji programu odtwarza wariant obciążenia odpowiadający pojedynczej operacji `piksel * 1.1` z Fazy 1, ale pomiary obu faz są odrębne. Wyników Fazy 1 nie przeliczano po zmianie programu; wszystkie pomiary Fazy 2 wykonano od początku z wykorzystaniem jego finalnej wersji. Wartości liczby operacji podawane dalej odnoszą się wyłącznie do zastosowanego modelu obciążenia i nie oznaczają równoważnej liczby dowolnych operacji procesora.

## Faza 2 – Poszukiwanie punktu opłacalności

### Metoda

Przed rozpoczęciem wyszukiwania wykonano `30` pomiarów kalibracyjnych dla jednej operacji na pikselu. Na podstawie mediany i rozstępu międzykwartylowego wyznaczono względną półszerokość typowego obszaru zmienności pomiarów:

`ε = IQR / (2 × mediana)`

Tak wyznaczone `ε` określa strefę stabilności pomiarowej wokół `1×`. Nie jest progiem praktycznej opłacalności wieloprocesowości. Po kalibracji jego wartość pozostawała stała przez cały eksperyment. Przyjęto przy tym, że względna zmienność zaobserwowana podczas kalibracji stanowi przybliżenie szumu pomiarowego dalszych pomiarów.

Właściwe wyszukiwanie rozpoczynano od kolejnego podwajania liczby operacji na pikselu. Dla każdego poziomu wykonano `7` prób, a decyzje oparto na medianie przyspieszenia.

Po znalezieniu przedziału, w którym mediana przyspieszenia przechodzi przez `1×`, zawężano go metodą hybrydową. W pierwszej kolejności wyznaczano przecięcie siecznej funkcji `f(k) = mediana przyspieszenia(k) - 1` z poziomem zerowym i wybierano najbliższą dopuszczalną liczbę operacji. Jeżeli po zaokrągleniu punkt nie leżał wewnątrz aktualnego przedziału lub wyznaczenie siecznej nie było możliwe, stosowano bisekcję. Dzięki temu wykorzystano informację o wartościach funkcji bez rezygnacji z bezpiecznego zawężania przedziału.

Procedurę powtarzano do zawężenia przedziału do dwóch sąsiednich wartości liczby operacji. Dla obu wykonano następnie po `30` prób oraz obliczono średnią, medianę, odchylenie standardowe, IQR i dwustronny `99%` przedział ufności dla przyspieszenia.

Przedział ufności wyznaczono na skali logarytmicznej i przekształcono z powrotem do skali przyspieszenia, co odpowiada ilorazowemu charakterowi tej miary.

Dalsze zwiększanie obciążenia zatrzymywano, jeżeli konserwatywne oszacowanie czasu następnego uruchomienia przekraczało `120 s`. Ograniczenie pełni wyłącznie funkcję bezpieczeństwa i nie stanowi założenia dotyczącego położenia punktu przejścia.

### Kalibracja

| Miara | Przyspieszenie |
| --- | ---: |
| Średnia | 0,138× |
| Mediana | 0,121× |
| Odchylenie standardowe | 0,044 |
| IQR | 0,029 |

Wyestymowane `ε`: `12,13%`.

Strefa stabilności pomiarowej: `0,879×–1,121×`.

### Wyszukiwanie

| Operacje na piksel | Sekwencyjnie – mediana | Wieloprocesowo – mediana | Przyspieszenie – mediana | Metoda |
| ---: | ---: | ---: | ---: | --- |
| 1 | 1,561 s | 12,430 s | 0,124× | wykładnicza |
| 2 | 1,760 s | 12,839 s | 0,137× | wykładnicza |
| 4 | 2,216 s | 12,461 s | 0,185× | wykładnicza |
| 8 | 3,126 s | 11,822 s | 0,263× | wykładnicza |
| 16 | 4,944 s | 12,388 s | 0,406× | wykładnicza |
| 32 | 9,895 s | 11,835 s | 0,884× | wykładnicza |
| 64 | 16,679 s | 13,620 s | 1,286× | wykładnicza |
| 33 | 11,298 s | 12,214 s | 0,940× | sieczna |
| 36 | 10,643 s | 11,333 s | 0,940× | sieczna |
| 37 | 10,927 s | 10,519 s | 1,030× | bisekcja |
| 41 | 26,492 s | 13,231 s | 1,932× | sieczna |

### Potwierdzenie

| Operacje | Średnia | Mediana | SD | IQR | 99% CI | Ocena |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 36 | 0,961× | 0,965× | 0,085 | 0,066 | 0,914×–1,001× | strefa stabilności pomiarowej |
| 37 | 1,382× | 1,250× | 0,387 | 0,704 | 1,154×–1,533× | przewaga wieloprocesowości |

### Analiza

Pomiary potwierdzające zawęziły badany obszar przejścia do `36–37` operacji na piksel w zastosowanym modelu obciążenia. Dla niższej z tych wartości nie można rozstrzygnąć przewagi żadnego sposobu wykonania. Wyznaczony przedział jedynie nieznacznie wykracza powyżej `1×` — jego górna granica wynosi `1,001×` — dlatego wynik pozostaje zgodny ze strefą stabilności pomiarowej.

Dla kolejnej dopuszczalnej wartości wyniki wskazują już na przewagę wieloprocesowości. Przedział skonstruowany metodą, która przy wielokrotnym powtarzaniu całej procedury obejmowałaby rzeczywistą wartość badanego parametru w około 99 przypadkach na 100, znajduje się w całości po stronie jej przewagi.

Nie wiadomo, jak zmieniłyby się granice przedziałów po przeprowadzeniu większej liczby pomiarów. W szczególności dla `36` operacji przedział mógłby w większym stopniu znaleźć się powyżej `1×`, przesunąć się w przeciwną stronę albo rozłożyć się wokół tej wartości bardziej symetrycznie. Uzyskane dane nie pozwalają rozstrzygnąć, który z tych wariantów wystąpiłby przy dokładniejszym oszacowaniu.

Ponieważ liczba operacji jest w tym eksperymencie wielkością dyskretną, pomiędzy `36` i `37` nie istnieje kolejna dopuszczalna wartość. W przyjętym modelu nie można więc dalej zawęzić badanego obszaru. Nie oznacza to również, że pojedyncza operacja o odpowiednio większym koszcie byłaby równoważna określonej liczbie powtórzeń operacji zastosowanej w eksperymencie.

## Wnioski końcowe

Wieloprocesowość nie gwarantuje skrócenia czasu wykonania tylko dlatego, że zadanie ma charakter obliczeniowy. O wyniku decyduje relacja między kosztem pracy możliwej do podziału a narzutem związanym z tworzeniem i organizacją procesów, serializacją oraz przekazywaniem danych.

W zależności od tej relacji możliwa jest przewaga wykonania sekwencyjnego, obszar, w którym różnica jest trudna do odróżnienia od naturalnej zmienności pomiarów, albo przewaga wieloprocesowości. Granice między tymi przypadkami nie są uniwersalne.

Wpływają na nie między innymi wydajność i architektura procesora, liczba dostępnych rdzeni i procesów roboczych, dostępna pamięć, system operacyjny i bieżące obciążenie komputera, a także rozmiar i reprezentacja danych, koszt pojedynczej operacji oraz koszt komunikacji między procesami.

Wyniki eksperymentu opisują więc zachowanie badanego programu w konkretnym środowisku wykonawczym. Zaobserwowany obszar `36–37` należy interpretować jako granicę uzyskaną dla zastosowanego modelu obciążenia, danych i warunków pomiarowych, a nie jako uniwersalny próg opłacalności wieloprocesowości. Eksperyment pokazuje natomiast ogólny mechanizm: przy odpowiednio dużym koszcie obliczeń oszczędność czasu wynikająca z ich równoległego wykonywania może przewyższyć narzut związany z wieloprocesowością.