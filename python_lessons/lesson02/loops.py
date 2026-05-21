pomiary_temp = [] # listę możemy stworzyć też tak -> (), ale nikt tego nie robi

# pętla for iteruje po zbiorze i zwraca kolejne elementy,
# a range() pozwala określić sumaryczną liczbę i aktualny numer iteracji
# Ctrl + C umożliwia przerwanie działania programu w trakcie wykonywania

for i in range(3):
    temp = float(input("Podaj mi, jaka jest obecnie temperatura: "))
    pomiary_temp.append(temp)
    
# CIEKAWOSTKA! W PĘTLI ISTNIEJE else, KTÓRY SIĘ URUCHOMI JAK ZAKOŃCZYMY WSZYSTKIE ITERACJE! 
# Czasami bardzo przydatne. Wykona się tylko wtedy, jeśli NIE BYŁO break.
else:
    print("Wszystkie pomiary zostały wprowadzone.")
    
print(pomiary_temp)
