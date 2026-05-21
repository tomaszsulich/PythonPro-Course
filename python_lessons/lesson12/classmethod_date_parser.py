class Data:
    
    def __init__(self, rok, mies, dzien):
        self.rok = rok
        self.mies = mies
        self.dzien = dzien
        
    @classmethod
    def ze_str(cls, data_str: str):
        "data_str format = 'DD-MM-RRRR'"
        mapped_to_ints = map(int, data_str.split('-'))
        lst_data = list(mapped_to_ints)[::-1]
        print(lst_data)
        return cls(*lst_data)
    

data = Data(1909, 3, 10)
data2 = Data.ze_str('19-03-2023')