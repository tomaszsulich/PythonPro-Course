# z dane.py wyciagamy sobie nazwy obecnosc i uczniowie. teraz mamy do nich dostep w tym pliku
from dane import obecnosc, uczniowie

""" Przejrzyj dane i wyszukaj w nich informacje:
- o klasie z najlepszą obecnością, DONE
- najlepszym uczniu z każdej klasy, DONE
- najlepszym uczniu ogółem, DONE
- czy któraś z klas miała średnią min 4.75? DONE
- czy któraś z klas miała obecność minimum 90%? DONE
- wskaż uczniów ze średnią minimum 4.0 którzy jednocześnie nie mają żadnej oceny poniżej -3. DONE
- policz wynik klasy i posortuj klasę malejąco względem wzoru `wynik = średnia_ocen * 0.7 + obecność * 0.3` DONE
- wskaż najtrudniejszy i najłatwiejszy przedmiot (najniższa i najwyższa srednia ocen) DONE
- wskaż leniwych ale zdolnych (obecość <70%, ocena >=4.5) i pracowitych ale nie tak zdolnych (obecność >=90%, ocena <3.5) DONE
- uczniów z tylko kiepskimi ocenami (żadna z ocen nie przekracza 3.3) DONE
- wymień uczniów, którzy byli obecni co najmniej 10 dni pod rząd DONE
"""

# uczniowie = (uczniowie.replace(",", "\n")).splitlines() NIE ZADZIAŁA BO ENTERY SĄ ZAMASKOWANE, WIĘC NIE MUSIMY ICH DODAWAĆ RĘCZNIE!!!

# Wczytanie i przygotowanie danych
def wczytaj_uczniow(uczniowie: str) -> list[dict]:
    uczniowie = uczniowie.splitlines()
    uczniowie_tabela = [linia.split(";") for linia in uczniowie if linia.strip()]
    
    opis_uczniow = uczniowie_tabela[0]
    dane_uczniow = uczniowie_tabela[1:]
    
    uczniowie_slowniki = []
    
    for dane_ucznia in dane_uczniow:
        uczen = dict(zip(opis_uczniow, dane_ucznia))
        
        for przedmiot in opis_uczniow[2:]:
            uczen[przedmiot] = uczen[przedmiot].split("|")
            
        uczniowie_slowniki.append(uczen)
        
    return uczniowie_slowniki

def polacz_obecnosc_z_uczniami(uczniowie_slowniki: list, obecnosc: dict) -> list[dict]:
    for uczen in uczniowie_slowniki:
        imie = uczen["imie"]
        
        if imie in obecnosc:
            uczen["obecnosc"] = obecnosc[imie]
        else:
            uczen["obecnosc"] = []
            
    return uczniowie_slowniki

# Pobieranie danych pomocniczych
def pobierz_klasy(uczniowie_slowniki: list[dict]) -> list[str]:
    return sorted(
        {
            uczen["klasa"] 
            for uczen in uczniowie_slowniki
        }
    )

def pobierz_oceny_ucznia(uczen: dict) -> list[str]:
    oceny = []
    
    for klucz, wartosc in uczen.items():
        if klucz in ["imie", "klasa", "obecnosc"]:
            continue
        oceny += wartosc
        
    return oceny

def pobierz_przedmioty(uczniowie_slowniki: list[dict]) -> list[str]:
    return [
        klucz
        for klucz in uczniowie_slowniki[0]
        if klucz not in ["imie", "klasa", "obecnosc"]
    ]

# Obliczenia bazowe
def wartosc_oceny(ocena: str) -> float:
    if "+" in ocena:
        return int(ocena[0]) + 0.3
    elif "-" in ocena:
        return int(ocena[0]) - 0.3
    return int(ocena)

def srednia_ucznia(uczen: dict) -> float:
    oceny = pobierz_oceny_ucznia(uczen)
    wartosci = [wartosc_oceny(ocena) for ocena in oceny]
    
    return sum(wartosci) / len(wartosci)

def srednia_klasy(uczniowie_slowniki: list[dict], klasa: str) -> float:
    suma = 0
    licznik = 0
    
    for uczen in uczniowie_slowniki:
        if uczen["klasa"] == klasa:
            suma += srednia_ucznia(uczen)
            licznik += 1
            
    return suma / licznik

def frekwencja_klasy(uczniowie_slowniki: list[dict], klasa: str) -> float:
    obecnosci = 0
    wszystkie = 0
    
    for uczen in uczniowie_slowniki:
        if uczen["klasa"] == klasa:
            obecnosci += uczen["obecnosc"].count("I")
            wszystkie += len(uczen["obecnosc"])
            
    return obecnosci / wszystkie

# Funkcje analityczne
def klasa_najlepsza_obecnosc(uczniowie_slowniki: list[dict]) -> tuple[str, int]:
    obecnosci_klas = {}
    
    for uczen in uczniowie_slowniki:
        klasa = uczen["klasa"]
        obecnosci = uczen["obecnosc"]
        
        liczba_obecnosci = 0
        for status in obecnosci:
            if status == "I":
                liczba_obecnosci += 1
                
        if klasa in obecnosci_klas:
            obecnosci_klas[klasa] += liczba_obecnosci
        else:
            obecnosci_klas[klasa] = liczba_obecnosci
            
    najlepsza_klasa = None
    max_obecnosci = 0
    
    for klasa, suma in obecnosci_klas.items():
        if suma > max_obecnosci:
            max_obecnosci = suma
            najlepsza_klasa = klasa
            
    return najlepsza_klasa, max_obecnosci

def najlepszy_uczen_w_klasie(uczniowie_slowniki: list[dict], klasa: str) -> tuple[str, float]:
    najlepszy = None
    najlepsza_srednia = 0
    
    for uczen in uczniowie_slowniki:
        if uczen["klasa"] != klasa:
            continue
        
        srednia = srednia_ucznia(uczen)
        
        if srednia > najlepsza_srednia:
            najlepsza_srednia = srednia
            najlepszy = uczen["imie"]
            
    return najlepszy, najlepsza_srednia

def najlepszy_uczen(uczniowie_slowniki: list[dict]) -> tuple[str, str, float]:
    najlepszy = None
    najlepsza_srednia = 0
    
    for uczen in uczniowie_slowniki:
        srednia = srednia_ucznia(uczen)
        
        if srednia > najlepsza_srednia:
            najlepsza_srednia = srednia
            najlepszy = uczen
            
    return najlepszy["imie"], najlepszy["klasa"], najlepsza_srednia

def znajdz_leniwych_i_pracowitych(uczniowie_slowniki: list[dict]) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    leniwi_zdolni = {}
    pracowici_mniej_zdolni = {}
    
    for uczen in uczniowie_slowniki:
        srednia = srednia_ucznia(uczen)
        
        frekwencja_ucznia = uczen["obecnosc"].count("I") / len(uczen["obecnosc"])
        klasa = uczen["klasa"]
        imie = uczen["imie"]
        
        # leniwy, ale zdolny
        if frekwencja_ucznia < 0.7 and srednia >= 4.5:
            if klasa not in leniwi_zdolni:
                leniwi_zdolni[klasa] = []
            leniwi_zdolni[klasa].append(imie)
            
        # pracowity, ale nie tak zdolny
        elif frekwencja_ucznia >= 0.9 and srednia < 3.5:
            if klasa not in pracowici_mniej_zdolni:
                pracowici_mniej_zdolni[klasa] = []
            pracowici_mniej_zdolni[klasa].append(imie)
    
    return leniwi_zdolni, pracowici_mniej_zdolni

# Formatowanie tekstu
def forma_ucznia(imie: str) -> tuple[str, str, str, str]:
    if imie.endswith("a"):
        return "uczennicą", "osiągnęła", "która", "najlepszą"
    return "uczniem", "osiągnął", "który", "najlepszym"

def formatuj_liste(elementy: list[str]) -> str:
    if len(elementy) == 1:
        return elementy[0]
    return ", ".join(elementy[:-1]) + " oraz " + elementy[-1]

def formatuj_grupy(dane: dict[str, list[str]]) -> str:
    grupy = []
    
    for klasa, uczniowie in dane.items():
        opis_uczniow = formatuj_liste(uczniowie)
        grupy.append(f"{opis_uczniow} z klasy {klasa}")
    
    return formatuj_liste(grupy)

# Wyświetlanie wyników
def wyswietl_klasy_z_wysoka_srednia(uczniowie_slowniki: list[dict]) -> None:
    znaleziono = False
    
    for klasa in pobierz_klasy(uczniowie_slowniki):
        if srednia_klasy(uczniowie_slowniki, klasa) > 4.75:
            print(f"Klasa {klasa} ma średnią powyżej 4.75.")
            znaleziono = True
                
    if not znaleziono:
        print("Żadna klasa nie ma średniej powyżej 4.75.")

def wyswietl_klasy_z_wysoka_obecnoscia(uczniowie_slowniki: list[dict]) -> bool:
    znaleziono = False
    
    for klasa in pobierz_klasy(uczniowie_slowniki):
        if frekwencja_klasy(uczniowie_slowniki, klasa) >= 0.9:
            print(f"Klasa {klasa} ma minimum 90% obecności.")
            znaleziono = True
            
    if not znaleziono:
        print(f"Żadna klasa nie osiągnęła minimum 90% obecności.")
    
    return znaleziono

def wyswietl_ranking_klas(uczniowie_slowniki: list[dict]) -> None:
    ranking = []
    
    for klasa in pobierz_klasy(uczniowie_slowniki):
        srednia_ocen = srednia_klasy(uczniowie_slowniki, klasa)
        frekwencja = frekwencja_klasy(uczniowie_slowniki, klasa)
        
        wynik = srednia_ocen * 0.7 + frekwencja * 0.3
        ranking.append((klasa, wynik))
        
    ranking = sorted(ranking, key = lambda x: x[1], reverse = True)
    print(f"\n\n ===RANKING KLAS (70% średnia + 30% frekwencja)=== \n")
    
    for i, (klasa, wynik) in enumerate(ranking, 1):
        print(f"{i}. {klasa} - {wynik:.2f}")
    print("\n")

def wyswietl_najlepszych_uczniow(uczniowie_slowniki: list[dict]) -> None:
    for klasa in pobierz_klasy(uczniowie_slowniki):
        imie_klasa, srednia_klasa = najlepszy_uczen_w_klasie(uczniowie_slowniki, klasa)
        rola_klasa, czasownik_klasa, zaimek_klasa, przymiotnik_klasa = forma_ucznia(imie_klasa)
        
        print(f"W klasie {klasa} {przymiotnik_klasa} {rola_klasa} jest {imie_klasa}, {zaimek_klasa} {czasownik_klasa} średnią {srednia_klasa:.2f}.")

def wyswietl_mocnych_uczniow(uczniowie_slowniki: list[dict]) -> None:
    znaleziono = False
    print("Uczniowie z wysoką średnią i bez słabych ocen:\n")

    for uczen in uczniowie_slowniki:
        srednia = srednia_ucznia(uczen)
        oceny = pobierz_oceny_ucznia(uczen)
        
        brak_slabych = True
        
        for ocena in oceny:
            if wartosc_oceny(ocena) < 2.7:
                brak_slabych = False
                break
        
        if srednia >= 4.0 and brak_slabych:
            print(f"{uczen['imie']} z klasy {uczen['klasa']} ma średnią minimum 4.0 i brak ocen poniżej 3-.")
            znaleziono = True
            
    if not znaleziono:
            print("Żaden uczeń nie osiągnął średniej minimum 4.0 i ocen poniżej 3-.")
    print("\n")

def wyswietl_leniwych_i_pracowitych(uczniowie_slowniki: list[dict]) -> None:
    leniwi_zdolni, pracowici = znajdz_leniwych_i_pracowitych(uczniowie_slowniki)
    
    if leniwi_zdolni:
        print(f"{formatuj_grupy(leniwi_zdolni)} to uczniowie leniwi, ale zdolni.")
    else:
        print("Brak uczniów, którzy są leniwi, ale zdolni.")  
        
    if pracowici:
        print(f"{formatuj_grupy(pracowici)} to uczniowie pracowici, ale nie tak zdolni.")
    else:
        print("Brak uczniów, którzy są pracowici, ale nie tak zdolni.")
    print("\n")

def wyswietl_kiepskich_uczniow(uczniowie_slowniki: list[dict]) -> None:
    znaleziono = False
    print("Uczniowie z wyłącznie słabymi ocenami:\n")
    
    for uczen in uczniowie_slowniki:
        oceny = pobierz_oceny_ucznia(uczen)
        tylko_kiepskie = True
        
        for ocena in oceny:
            if wartosc_oceny(ocena) > 3.3:
                tylko_kiepskie = False
                break
            
        if tylko_kiepskie:
            print(f"{uczen['imie']} z klasy {uczen['klasa']} ma tylko kiepskie oceny.")
            znaleziono = True
            
    if not znaleziono:
        print("Brak uczniów z samymi kiepskimi ocenami.")
    print("\n")

def wyswietl_uczniow_z_ciagiem_obecnosci(uczniowie_slowniki: list[dict]) -> None:
    znaleziono = False
    print("Uczniowie z ciągiem obecności (≥10 dni):\n")
    
    for uczen in uczniowie_slowniki:
        obecnosci = uczen["obecnosc"]
        
        max_ciag = 0
        aktualny_ciag = 0
        
        for status in obecnosci:
            if status == "I":
                aktualny_ciag += 1
                if aktualny_ciag > max_ciag:
                    max_ciag = aktualny_ciag
            else:
                aktualny_ciag = 0
                
        if max_ciag >= 10:
            czasownik = "miała" if uczen["imie"].endswith("a") else "miał"
            print(f"{uczen['imie']} z klasy {uczen['klasa']} {czasownik} co najmniej 10 dni obecności pod rząd.")
            znaleziono = True
            
    if not znaleziono:
        print("Brak uczniów obecnych co najmniej 10 dni pod rząd.")
    print("\n")
  
def wyswietl_skrajne_przedmioty(uczniowie_slowniki: list[dict]) -> None:
    przedmioty = pobierz_przedmioty(uczniowie_slowniki)
    srednie_przedmiotow = []
    
    for przedmiot in przedmioty:
        oceny = []
        
        for uczen in uczniowie_slowniki:
            oceny += uczen[przedmiot]
            
        wartosci = [wartosc_oceny(o) for o in oceny]
        srednia_przedmiotu = sum(wartosci) / len(wartosci)
        
        srednie_przedmiotow.append((przedmiot, srednia_przedmiotu))
        
    najtrudniejszy = min(srednie_przedmiotow, key = lambda x: x[1])
    najlatwiejszy = max(srednie_przedmiotow, key = lambda x: x[1])
    
    print(f"Najtrudniejszym przedmiotem jest {najtrudniejszy[0]} ze średnią {najtrudniejszy[1]:.2f}.")
    print(f"Najłatwiejszym przedmiotem jest {najlatwiejszy[0]} ze średnią {najlatwiejszy[1]:.2f}.")


def main():
    uczniowie_slowniki = wczytaj_uczniow(uczniowie)
    uczniowie_slowniki = polacz_obecnosc_z_uczniami(uczniowie_slowniki, obecnosc)
    
    klasa, wynik = klasa_najlepsza_obecnosc(uczniowie_slowniki)
    print(f"Najlepszą frekwencję osiągnęła klasa {klasa} (łącznie {wynik} obecności).")
    
    wyswietl_klasy_z_wysoka_srednia(uczniowie_slowniki)
    wyswietl_klasy_z_wysoka_obecnoscia(uczniowie_slowniki)
    wyswietl_ranking_klas(uczniowie_slowniki)
    
    wyswietl_najlepszych_uczniow(uczniowie_slowniki)
    
    imie_ogol, klasa_ogol, srednia_ogol = najlepszy_uczen(uczniowie_slowniki)
    rola_ogol, czasownik_ogol, zaimek_ogol, przymiotnik_ogol = forma_ucznia(imie_ogol)
    print(f"W całej szkole {przymiotnik_ogol} {rola_ogol} jest {imie_ogol} z klasy {klasa_ogol}, {zaimek_ogol} {czasownik_ogol} średnią {srednia_ogol:.2f}. \n\n")
    
    wyswietl_mocnych_uczniow(uczniowie_slowniki)
    wyswietl_leniwych_i_pracowitych(uczniowie_slowniki)
    wyswietl_kiepskich_uczniow(uczniowie_slowniki)
    wyswietl_uczniow_z_ciagiem_obecnosci(uczniowie_slowniki)
        
    wyswietl_skrajne_przedmioty(uczniowie_slowniki)


if __name__ == "__main__":
    main()