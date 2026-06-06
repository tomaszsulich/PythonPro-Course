from sqlalchemy import Column, Integer, String, Boolean, DateTime
import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() # Klasa bazowa dla naszych modeli

class Zadanie(Base):
    __tablename__ = 'zadania' # Nazwa tabeli w bazie danych
    id = Column(Integer, primary_key=True)
    opis = Column(String, nullable=False)
    zrobione = Column(Boolean, default=False, nullable=False)
    data_utworzenia = Column(DateTime, default = datetime.datetime.utcnow)
    
    def __repr__(self):
        return f"<Zadanie(id={self.id}, opis='{self.opis}', zrobione={self.zrobione}, data_utworzenia={self.data_utworzenia})>"