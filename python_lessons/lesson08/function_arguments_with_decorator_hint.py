# @mierz_czas
def stworz_uzytkownika(nick: str,
                       imie: str,
                       punkty_premium: float = 0,
                       serwer = "eu"):
    print("tworzę użytkownika", nick, imie, punkty_premium, serwer)
    

stworz_uzytkownika(nick = "rafal", imie = "rafal", punkty_premium = 0, serwer = "ch")