class BladWalidacjiError(Exception):
    ...
    

def walidacja_hasla(haslo: str):
    # waliduje hasło
    err_lst = []
    # długość
    if len(haslo) < 8:
        err_lst.append("Hasło za krótkie, wymagane min. 8 znaków.")
    if not any(znak.isupper() for znak in haslo):
        err_lst.append("Brak dużej litery!")
    if not any(znak.isdigit() for znak in haslo):
        err_lst.append("Brak cyfry w haśle!")
    if any(znak.isalnum() for znak in haslo):
        err_lst.append("Brak znaku specjalnego!")
    if err_lst:
        raise BladWalidacjiError(*err_lst)
    

try:
    walidacja_hasla("xd")
except BladWalidacjiError as e:
    bledy = e