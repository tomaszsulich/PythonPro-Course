class Niepelnoletni(Exception):
    ...
    
def nalej_piwa(wiek_pijacego):
    if wiek_pijacego < 18:
        # podnoszenie własnego wyjątku
        raise Niepelnoletni("żeby napić się piwa, musisz mieć 18 lat!")
    print("nalewa piwo...")
    
nalej_piwa(20)
nalej_piwa(10)