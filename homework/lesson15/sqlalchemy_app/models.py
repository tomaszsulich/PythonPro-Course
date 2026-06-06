from sqlalchemy import Column, Integer, String, Boolean, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() # Klasa bazowa dla naszych modeli

zadania_tagi = Table(
    "zadania_tagi",
    Base.metadata,
    Column("zadanie_id", Integer, ForeignKey("zadania.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tagi.id"), primary_key=True)
)

class Zadanie(Base):
    __tablename__ = 'zadania' # Nazwa tabeli w bazie danych
    
    id = Column(Integer, primary_key=True)
    opis = Column(String, nullable=False)
    zrobione = Column(Boolean, default=False, nullable=False)
    data_utworzenia = Column(DateTime, default = datetime.datetime.utcnow)
    
    tagi = relationship(
        "Tag",
        secondary=zadania_tagi,
        back_populates="zadania"
    )
    
    def __repr__(self):
        return f"<Zadanie(id={self.id}, opis='{self.opis}', zrobione={self.zrobione})>"
    
class Tag(Base):
    __tablename__ = 'tagi'
    
    id = Column(Integer, primary_key=True)
    nazwa = Column(String, nullable=False, unique=True)
    
    zadania = relationship(
        "Zadanie",
        secondary=zadania_tagi,
        back_populates="tagi"
    )