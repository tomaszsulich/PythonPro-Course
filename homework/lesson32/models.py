from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import (
    DeclarativeBase, 
    Mapped, 
    mapped_column,
    relationship,
    validates,
)
from typing import Any


# --- Definicje Modeli ---
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "app_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(100))

    # Task 20 (challenge) - relacja użytkownika z produktami
    products: Mapped[list["Product"]] = relationship(
        back_populates="user"
    )

    def to_dict(self) -> dict[str, int | str]:
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }


# Task 9 (challenge) - model Product
class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer)

    # Task 20 (challenge) - relacja produktu z twórcą
    user_id: Mapped[int] = mapped_column(
        ForeignKey("app_users.id")
    )
    user: Mapped["User"] = relationship(
        back_populates="products"
    )

    @validates("price")
    def validate_price(self, _key: str, value: Any) -> int:
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(
                "Cena musi być liczbą całkowitą wyrażoną w groszach."
            )

        if value < 0:
            raise ValueError("Cena nie może być ujemna.")

        return value

    def to_dict(self) -> dict[str, int | str]:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }


# Task 16 (challenge) - model Account
class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    balance: Mapped[int] = mapped_column(Integer)