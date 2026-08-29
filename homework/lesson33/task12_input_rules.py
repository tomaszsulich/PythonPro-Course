from fastapi import FastAPI
from pydantic import BaseModel, field_validator


app = FastAPI()


class Product(BaseModel):
    name: str
    price: float
    category: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not value.isalnum():
            raise ValueError(
                "Nazwa może zawierać tylko litery i cyfry."
            )

        return value

    @field_validator("price")
    @classmethod
    def validate_price(cls, value: float) -> float:
        if not 0 < value <= 10_000:
            raise ValueError(
                "Cena musi być większa od 0 i nie większa niż 10 000."
            )

        return value

    @field_validator("category")
    @classmethod
    def validate_category(cls, value: str) -> str:
        allowed_categories = ["Electronics", "Books", "Clothing"]

        if value not in allowed_categories:
            raise ValueError(
                f"Kategoria musi być jedną z: {', '.join(allowed_categories)}."
            )

        return value


@app.post("/products")
async def create_product(product: Product) -> Product:
    return product