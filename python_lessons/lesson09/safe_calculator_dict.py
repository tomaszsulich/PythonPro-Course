while True:
    try:
        fnum = float(input("Podaj pierwszą liczbę: "))
        snum = float(input("Podaj drugą liczbę: "))
        dzialanie = input("Podaj działanie [+, -, *, /]: ")
        func_dict = {"+": lambda x, y: x + y,
                    "-": lambda x, y: x - y,
                    "*": lambda x, y: x * y, 
                    "/": lambda x, y: x / y}
        # krótsze zastępstwo dla if'ów
        func_dict[dzialanie](fnum, snum)
    except ValueError:
        print("Podano niepoprawną liczbę!")
    except KeyError:
        print("Niepoprawne działanie!")
    except ZeroDivisionError:
        print("Druga liczba nie może być równa zero w przypadku dzielenia!")
    finally:
        print("Runda kolejna!")