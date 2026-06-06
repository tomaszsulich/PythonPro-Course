from dataclasses import dataclass, field
from typing import ClassVar
import sqlite3

@dataclass
class Produkt:
    tabela: ClassVar[str] = "produkty"
    
    id_produktu: int = field()
    nazwa_produktu: str
    cena: float
    
    def pobierz_wszystkie_produkty(model: Produkt):
        fields_ = [f
                   for f in Produkt.__dataclass_fields__.keys()
                   if f != "tabela"]
        cols = ", ".join(fields_)
        
        qr = f"""--sql
        SELECT {cols}
        FROM ?
        """
        with sqlite3.connect("sklep.db") as conn:
            c = conn.cursor()
            return c.execute(qr, (model.tabela, )).fetchall()


if __name__ == "__main__":
    for wiersz in Produkt.pobierz_wszystkie_produkty(Produkt):
        print(wiersz)   
        