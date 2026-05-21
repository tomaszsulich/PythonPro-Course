def sprawdz_haslo(haslo: str) -> bool:
    """
    Sprawdza, czy hasło spełnia podstawowe wymagania bezpieczeństwa.
    
    Warunki:
    - co najmniej 8 znaków
    - przynajmniej jedna wielka litera
    - przynajmniej jedna cyfra
    
    Args:
        haslo (str): hasło do sprawdzenia
        
    Returns:
        bool: True, jeśli hasło spełnia wszystkie warunki, w przeciwnym razie False
    """
    ma_wielka = False
    ma_cyfre = False
    
    for znak in haslo:
        if znak.isupper():
            ma_wielka = True
        if znak.isdigit():
            ma_cyfre = True
            
    return len(haslo) >= 8 and ma_wielka and ma_cyfre

print(sprawdz_haslo("Haslo123")) # True
print(sprawdz_haslo("haslo123")) # False (brak wielkiej litery)
print(sprawdz_haslo("Hasloabc")) # False (brak cyfry)
print(sprawdz_haslo("Has1")) # False (za krótkie)

# WERSJA Z NADPISYWANIEM WARTOŚCI TYLKO RAZ - SZYBSZE DZIAŁANIE
# def sprawdz_haslo(haslo: str) -> bool:
#     """
#     Sprawdza, czy hasło spełnia podstawowe wymagania bezpieczeństwa.
    
#     Warunki:
#     - co najmniej 8 znaków
#     - przynajmniej jedna wielka litera
#     - przynajmniej jedna cyfra
    
#     Args:
#         haslo (str): hasło do sprawdzenia
        
#     Returns:
#         bool: True, jeśli hasło spełnia wszystkie warunki, w przeciwnym razie False
#     """
#     if len(haslo) < 8:
#         return False
    
#     ma_wielka = False
#     ma_cyfre = False
    
#     for znak in haslo:
#         if not ma_wielka and znak.isupper():
#             ma_wielka = True
#         if not ma_cyfre and znak.isdigit():
#             ma_cyfre = True
#         if ma_wielka and ma_cyfre:
#             return True

#     return False
    
# print(sprawdz_haslo("Haslo123")) # True
# print(sprawdz_haslo("haslo123")) # False (brak wielkiej litery)
# print(sprawdz_haslo("Hasloabc")) # False (brak cyfry)
# print(sprawdz_haslo("Has1")) # False (za krótkie)

# WERSJA Z ENUMERATE, KTÓRE JEST KORZYSTNIEJSZE, GDY OPERUJEMY NA OGROMNEJ ILOŚCI DANYCH,
# GDY LEN() JEST KOSZTOWNY I/ALBO GDY I TAK MUSIMY PRZEJŚĆ PO WSZYSTKICH ELEMENTACH
# def sprawdz_haslo(haslo: str) -> bool:
#     """
#     Sprawdza, czy hasło spełnia podstawowe wymagania bezpieczeństwa.
    
#     Warunki:
#     - co najmniej 8 znaków
#     - przynajmniej jedna wielka litera
#     - przynajmniej jedna cyfra
    
#     Args:
#         haslo (str): hasło do sprawdzenia
        
#     Returns:
#         bool: True, jeśli hasło spełnia wszystkie warunki, w przeciwnym razie False
#     """
#     ma_wielka = False
#     ma_cyfe = False
#     dlugosc = 0
    
#     for dlugosc, znak in enumerate(haslo, start=1):
#         if not ma_wielka and znak.isupper():
#             ma_wielka = True
#         if not ma_cyfre and znak.isdigit():
#             ma_cyfre = True
            
#         if dlugosc >= 8 and ma_wielka and ma_cyfre:
#             return True
        
#         return False

# print(sprawdz_haslo("Haslo123")) # True
# print(sprawdz_haslo("haslo123")) # False (brak wielkiej litery)
# print(sprawdz_haslo("Hasloabc")) # False (brak cyfry)
# print(sprawdz_haslo("Has1")) # False (za krótkie)