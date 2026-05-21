class Data:
    
    def __init__(self, rok: int, mies: int, dzien: int) -> None:
        self.rok = rok
        self.mies = mies
        self.dzien = dzien
        
    @classmethod
    def ze_stringa(cls, data_str: str) -> "Data":
        """Tworzy obiekt Data z napisu w formacie DD-MM-RRRR"""
        
        
        dzien, mies, rok = map(int, data_str.split('-'))
        return cls(rok, mies, dzien)
    
    def __str__(self) -> str:
        return f"{self.dzien:02d}-{self.mies:02d}-{self.rok}"


def main() -> None:    
    data1 = Data(1909, 3, 10)
    data2 = Data.ze_stringa('19-03-2023')
    
    print(data1)
    print(data2)
    

if __name__ == "__main__":
    main()