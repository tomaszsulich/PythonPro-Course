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
    co_najmniej_jedna_wielka = False
    co_najmniej_jedna_cyfra = False
    
    for znak in haslo:
        if znak.isupper():
            co_najmniej_jedna_wielka = True
        if znak.isdigit():
            co_najmniej_jedna_cyfra = True
            
    return len(haslo) >= 8 and co_najmniej_jedna_wielka and co_najmniej_jedna_cyfra

print(sprawdz_haslo("Haslo123")) # True
print(sprawdz_haslo("haslo123")) # False (brak wielkiej litery)
print(sprawdz_haslo("Hasloabc")) # False (brak cyfry)
print(sprawdz_haslo("Has1")) # False (za krótkie)