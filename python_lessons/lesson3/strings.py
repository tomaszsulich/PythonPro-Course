tekst = " Witaj python! "
print(tekst.strip())

# MAKSYMALNA LICZBA ZMIAN
tekst_2 = " witaj pytaahosanya! "
print(tekst_2.replace("a", "x", 1))

# CZYM RÓŻNIĄ SIĘ FUNKCJE OD METOD? - BARDZO ZDAWKOWO PROWADZĄCY POWIEDZIAŁ
print(tekst["5"] == "Witaj", tekst.startswith("Witaj"))