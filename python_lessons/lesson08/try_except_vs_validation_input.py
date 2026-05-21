input_int = int(input("Podaj inta:")) # dla 'a' np. program się wywali

input_int = input("Podaj inta: ")
if all(char.isdigit() for char in input_int):
    int_int = int(input_int) # ale mało czytelne
    
try:
    int_int = int(input("Podaj inta: "))
except ValueError:
    print("podano niepoprawną liczbę całkowitą")
except Exception:
    print("wyjątek ostateczny") # raczej się z niego nie korzysta