class TestyTelewizor:
    
    @classmethod
    def testuj_telewizor(cls, marka, ekran, odwzorowanie_kolorow):
        cls.testuj_odwzorowanie_kolorow(odwzorowanie_kolorow)
        cls.testuj_ekran(ekran)
        cls.testuj_marke(marka)
        
    @staticmethod
    def testuj_odwzorowanie_kolorow(odwzorowanie_kolorow):
        ...
    
    @staticmethod
    def testuj_marke(marka):
        ...
        
    @staticmethod
    def testuj_ekran(ekran):
        ...
        
TestyTelewizor.testuj_ekran()
TestyTelewizor.testuj_marke()