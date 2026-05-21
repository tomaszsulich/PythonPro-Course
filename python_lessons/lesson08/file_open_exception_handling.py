def wczytaj_plik(sciezka_do_pliku: str, mode = "r"):
    plik = None
    try:
        plik = open(sciezka_do_pliku, mode = mode)
    except FileNotFoundError:
        print("plik nie istnieje")
    except OSError:
        print("sciezka_do_pliku musi być typu str!")
    except ValueError:
        print("podano niepoprawny parametr")
    # podstawowy wyjątek
    except Exception:
        print("nieprzewidziany błąd! skontaktuj się z programistą")
    # żaden z powyższych wyjątków nie wystąpił
    else:
        print("else ale czemu?!")
    # finally to blok, który się zawsze wykona
    finally:
        print("finally")
    return plik