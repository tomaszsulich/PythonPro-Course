from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite:///products.db'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    """
    Modeluje produkt przechowywany w bazie danych.
    
    Grupuje atrybuty identyfikujące ofertę oraz stanowi
    warstwę pośredniczącą pomiędzy logiką aplikacji 
    a strukturą tabeli.
    """
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    
    @classmethod
    def create(cls, name: str, company: str, price: float) -> Product | None:
        """
        Koordynuje proces walidacji i rejestracji produktu.
        
        Weryfikuje poprawność danych wejściowych,
        zapobiega tworzeniu duplikatów oraz zapisuje
        nowy rekord w bazie danych po pomyślnym
        zakończeniu wszystkich etapów kontroli.
        """
        
        errors: list[str] = []
        
        if not name.strip():
            errors.append("Nazwa produktu nie może być pusta!")
        if not company.strip():
            errors.append("Nazwa firmy nie może być pusta!")
        if price <= 0:
            errors.append("Cena musi być większa od zera!")
        
        if errors:
            for error in errors:
                print(error)
            return None
        
        normalized_name = name.strip().title()
        normalized_company = company.strip().title()
        
        existing_product = cls.query.filter_by(
            name = normalized_name,
            company = normalized_company,
            price = price
        ).first()
        
        if existing_product:
            print("Taki produkt już istnieje.")
            return existing_product
        
        product = cls (
            name = normalized_name,
            company = normalized_company,
            price = price,
        )
        
        db.session.add(product)
        db.session.commit()
        
        return product
    
    def __repr__(self) -> str:
        return f'<{self.name} {self.company}: {self.price}>'
    
with app.app_context():
    db.create_all()