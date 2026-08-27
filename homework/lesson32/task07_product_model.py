from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, validates
from typing import Any


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer)

    @validates("price")
    def validate_price(self, _key: str, value: Any) -> int:
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(
                "Cena musi być liczbą całkowitą wyrażoną w groszach."
            )

        if value < 0:
            raise ValueError("Cena nie może być ujemna.")

        return value