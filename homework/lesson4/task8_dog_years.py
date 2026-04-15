wiek_psa = float(input("Podaj wiek psa w latach: ").replace(",", "."))
    
if wiek_psa <= 0:
    print("Niepoprawny wiek psa.")
elif wiek_psa == 1:
    print(f"Twój pies ma {15} ludzkich lat.")
elif wiek_psa == 2:
    print(f"Twój pies ma {15 + 9} ludzkie lata.")
else:
    wiek_ludzki = 15 + 9 + (wiek_psa - 2) * 5
    print(f"Twój pies ma {wiek_ludzki:.2f} ludzkich lat.")
    
# ROZWIĄZANIE ALTERNATYWNE ZAPROPONOWANE PRZEZ ChatGPT, Z MOIMI DROBNYMI USPRAWNIENIAMI
# def wiek_psa_na_ludzki(wiek_psa: float) -> float | None:
#     if wiek_psa <= 0:
#         return None
#     elif wiek_psa <= 1:
#         return 15 * wiek_psa
#     elif wiek_psa <= 2:
#         return 15 + (wiek_psa - 1) * 9
#     return 24 + (wiek_psa - 2) * 5

# wiek_psa = float(input("Podaj wiek psa w latach: ").replace(",", "."))
# wynik = wiek_psa_na_ludzki(wiek_psa)

# if wynik is None:
#     print("Niepoprawny wiek psa.")
# else:
#     print(f"Twój pies ma {wynik:.2f} ludzkich lat.")

# ROZWIĄZANIE OD PAWŁA - BEZ FUNKCJI
# wiek = int(input("Podaj wiek psa: "))

# if wiek == 1:
#     print(f"Psa ma {15} lat")
# elif wiek == 2:
#     print(f"Psa ma {15 + 9} lat")
# else:
#     print("Psa ma", 15 + 9 + (wiek - 2) * 5, "lat")