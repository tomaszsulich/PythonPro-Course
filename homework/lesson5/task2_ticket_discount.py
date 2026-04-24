cena_biletu = 100

wiek = float(input("Ile masz lat? "))
czy_student = input("Czy jesteś studentem (tak/nie)? ").lower()

if wiek < 0:
    print("Wiek nie może być ujemny!")
elif wiek >= 0 and (wiek < 18 or czy_student == "tak"):
    cena_biletu /= 2
    print(f"Musisz zapłacić {cena_biletu:.2f} PLN." )
else:
    print(f"Musisz zapłacić {cena_biletu:.2f} PLN.")
    
# WERSJA CZYSTSZA, W KTÓREJ "UŻYJ AND I OR" TRAKTUJEMY JAKO SUGESTIĘ, A NIE WYMÓG
# cena_biletu = 100

# wiek = float(input("Ile masz lat? "))
# czy_student = input("Czy jesteś studentem (tak/nie)? ").lower()

# if wiek < 0:
#     print("Wiek nie może być ujemny!")
# elif wiek < 18 or czy_student == "tak":
#     cena_biletu /= 2
    
# print(f"Musisz zapłacić {cena_biletu:.2f} PLN.")

# WERSJA REALNA, NIE POD ZADANIE
# cena_biletu = 100

# wiek = float(input("Ile masz lat? "))

# if wiek < 0:
#     print("Wiek nie może być ujemny!")
# elif wiek < 18:
#     cena_biletu /= 2
# else:
#     czy_student = input("Czy jesteś studentem (tak/nie)? ").lower()
#     if czy_student == "tak":
#         cena_biletu /= 2

# print(f"Musisz zapłacić {cena_biletu:.2f} PLN.")