tak_odpowiedzi = {"tak", "t", "true", "prawda", "yes", "y"}
nie_odpowiedzi = {"nie", "n", "false", "fałsz", "no"}
dozwolone = tak_odpowiedzi | nie_odpowiedzi
ile_lat = int(input("Ile masz lat? "))

if ile_lat >= 18:
    while True:
        czy_prawo_jazdy = input("Masz prawo jazdy? ").lower()
        
        if czy_prawo_jazdy in dozwolone:
            break
        print("Wpisz tak/nie.")
else:
    czy_prawo_jazdy = "nie"
    
print(ile_lat >= 18 and czy_prawo_jazdy in tak_odpowiedzi)