przedstaw_sie_str = f"Hej, jestem {imie} i mam {wiek} lat."

przedstaw_sie_format = "Imię: {imie}, Wiek: {wiek}"

imie, wiek = "Pawel", 25

print(przedstaw_sie_format.format(imie = imie, wiek = wiek))

imie, wiek = "robert", 45

print(przedstaw_sie_format.format(imie = imie, wiek = wiek))

produkt, koszt = "chleb", 5.125

format_produktu = "{produkt} kosztuje {koszt:.2f}"
print(format_produktu.format(produkt = produkt, koszt = koszt))

print(f"{produkt} kosztuje {koszt:.2f}") # zaokrąglenie do 2 miejsc