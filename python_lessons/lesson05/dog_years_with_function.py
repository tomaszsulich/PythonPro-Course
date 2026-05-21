def dog_years(age: int) -> int:
    if age == 0:
        return 0
    elif age == 1:
        return 15
    elif age == 2:
        return 15 + 9
    elif age > 2:
        return 15 + 9 + (age - 2) * 5
    # tutaj zwracam None jako info, że wiek mi się nie podoba
    return None
    # mógłbym to zrobić w 'else', ale nie muszę, bo tak czy tak
    # jeżeli żaden warunek nie zostanie spełniony, to się ma wykonać

wiek = int(input("Podaj wiek psa: "))    
dy = dog_years(wiek)
if dy is None:
    print("Niepoprawny wiek psa!")
else:
    print(f"Pies ma {dog_years(wiek)} lat.")