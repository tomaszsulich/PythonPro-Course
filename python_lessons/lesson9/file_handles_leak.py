# w tle 10 plików, do których nie będzie dostępu, niemożliwe będzie zamknięcie, bo do pliku
# przypisany tylko ostatnio otworzony, reszta będzie w tle

pliki = [f"lesson9/safe_calculator_dict{i}.py"
         for i in range(10)]

for p in pliki:
    plik = open(p)