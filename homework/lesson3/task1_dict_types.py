imie = "tomek"
wiek = 26
oceny = [3, 2, 3, 5, 4]
czy_student = True
srednia_ocen = sum(oceny)/len(oceny)

student = {
    'imie': imie,
    'wiek': wiek,
    'sr_ocen': srednia_ocen,
    'czy_student': czy_student
}

def opisz_zmienna(zmienna):
    return f"{type(zmienna).__name__}"

for key, value in student.items():
    print(f"{key}: {value} ({opisz_zmienna(value)})")
