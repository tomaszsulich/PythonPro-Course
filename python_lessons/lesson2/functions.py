def func():
    return None

def pow(number):
    return number * number

def mul(number, number2):
    return number * number2

def czy_parzysta(liczba):
    return liczba % 2 == 0

#funkcje służą do wyizolowania jakiejś większej części kodu
def pole_kwadratu(bok):
    return bok * bok

def pole_trojkata(bok, wysokosc):
    return bok * wysokosc/2

figura = input("Jakiej figury pole chcesz policzyć?")
if figura == "trojkat":
    podstawa = 20
    wys = 10
    pole = pole_trojkata(podstawa, wys)
elif figura == "kwadrat":
    pole = pole_kwadratu(5)
    
# nie można podać argumentu po argumencie z wartością domyślną
# def pole_trojkata(podstawa=10, wysokosc):
#    return podstawa * wysokosc/2

def pole_trojkata(podstawa, wysokosc=10):
    return podstawa * wysokosc/2

print(pole_trojkata(20)) # używa domyślnej wysokości
print(pole_trojkata(20, 15)) #podajesz własną wartość
