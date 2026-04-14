# tutaj również można było użyć funkcji, ale czas mnie gonił
# def Celsjusz_to_Fahrenheit(temperatura_Celsjusz):
#    return temperatura_Celsjusz * 9/5 + 32

temperatura_Celsjusz = float(input("Podaj temperaturę w stopniach Celsjusza: "))

temperatura_Fahrenheit = temperatura_Celsjusz * 9/5 + 32

print(f"{temperatura_Celsjusz:.2f}°C to {temperatura_Fahrenheit:.2f}°F według wzoru F = C * 9/5 + 32.")

# WERSJA PODSTAWOWA - OD PAWŁA
# c = float(input("Podaj temperaturę w stopniach Celsjusza: "))

# f = c * 9 / 5 + 32

# print("Temperatura", c, "°C to", f, "°F")