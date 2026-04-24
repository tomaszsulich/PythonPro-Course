wiek = 20
# status = "Dorosły" if wiek >= 18 else "Niepełnoletni"

# mamy już stworzoną zmienną, w przypadku gdyby coś tam się podziało w środku...
status = "Niepełnoletni" # domyślna wartość, bardzo często się z niej korzysta
if wiek >= 18:
    status = "Dorosły"