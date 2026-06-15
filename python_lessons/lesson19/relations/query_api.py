from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, desc, asc, case, distinct, extract
from sqlalchemy.sql import label

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///one_to_many.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    products = db.relationship("Product", 
                               backref="category", 
                               lazy=True, 
                               cascade="all, delete-orphan")
    
    def __repr__(self):
        return f'<Category {self.name}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "product_count": len(self.products)
        }


class Product(db.Model):
    __tablename__ = "products"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=db.func.now())
    
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    
    def __repr__(self):
        return f"<Product {self.name} ({self.price} PLN)>"


def db_init():
    db.create_all()
    
    if not Category.query.first():
        elektronika = Category(name = "Elektronika", description = "Sprzęt elektroniczny")
        jedzenie = Category(name="Jedzenie", description="Produkty spożywcze")
        
        db.session.add_all([elektronika, jedzenie])
        db.session.flush() # żeby mieć elektronika.id
        
        laptop = Product(name = "Laptop Dell", price = 3500, category = elektronika)
        laptop2 = Product(name = "MacBook", price = 6000, category_id = elektronika.id)
        myszka = Product(name="Myszka", price=100, category=elektronika)
        monitor = Product(name="Monitor", price=900, category=elektronika)
        jablko = Product(name="Jabłko", price=1, category=jedzenie)
        parowki = Product(name="Parówki", price=15, category=jedzenie)
        sok_owocowy=Product(name="sok_owocowy", price=5, category=jedzenie)

        db.session.add_all([laptop, laptop2, jablko, parowki, sok_owocowy, myszka, monitor])
        db.session.commit()

     
def demo_read():
    kategoria = Category.query.filter_by(name="Elektronika").first()
    
    print(f"Kategoria: {kategoria.name}")
    for p in kategoria.products:
        print(f" - {p.name}: {p.price} PLN")
        
    produkt = Product.query.first()
    print(f"{produkt.name} jest w kategorii: {produkt.category.name}")

def agr_funcs():
    # 1. COUNT - Liczenie rekordów
    total_products = db.session.query(func.count(Product.id)).scalar()
    # SQL: SELECT COUNT(products.id) FROM products

    # 2. SUM - Suma
    total_value = db.session.query(func.sum(Product.price)).scalar()
    # SQL: SELECT SUM(products.price) FROM products

    # 3. AVG - Średnia
    avg_price = db.session.query(func.avg(Product.price)).scalar()
    # SQL: SELECT AVG(products.price) FROM products

    # 4. MIN / MAX
    cheapest = db.session.query(func.min(Product.price)).scalar()
    most_expensive = db.session.query(func.max(Product.price)).scalar()

    # 5. Wszystko naraz
    stats = db.session.query(
        func.count(Product.id).label('total'),
        func.sum(Product.price).label('value'),
        func.avg(Product.price).label('avg'),
        func.min(Product.price).label('min'),
        func.max(Product.price).label('max')
    ).first()

    print(f"""
    Statystyki magazynu:
    - Produktów: {stats.total}
    - Wartość: {stats.value:.2f} PLN
    - Średnia cena: {stats.avg:.2f} PLN
    - Najtańszy: {stats.min:.2f} PLN
    - Najdroższy: {stats.max:.2f} PLN
    """)
    
def groupby_stats():
    # Statystyki per kategoria
    stats_by_category = db.session.query(
        Category.name,
        func.count(Product.id).label('product_count'),
        func.sum(Product.price).label('total_value'),
        func.avg(Product.price).label('avg_price')
    ).join(Product).group_by(Category.name).all()

    # Wynik:
    # [('Elektronika', 50, 125000.00, 2500.00), ('Książki', 30, 1500.00, 50.00)]

    for stat in stats_by_category:
        print(f"""
        Kategoria: {stat.name}
        - Produktów: {stat.product_count}
        - Wartość: {stat.total_value:.2f} PLN
        - Średnia: {stat.avg_price:.2f} PLN
        """)
        
def having_func():
    popular_categories = db.session.query(
        Category.name,
        func.count(Product.id).label('count')
        ).join(Product).group_by(Category.name).having(
            func.count(Product.id) >= 3
        ).all()
    return popular_categories

def case_when():
    db.session.query(Product)
    price_distribution = db.session.query(
    case(
        (Product.price < 50, 'Tanie'),
        (Product.price < 200, 'Średnie'),
        (Product.price < 1000, 'Drogie'),
        else_='Premium'
        ).label('price_range'),
        func.count(Product.id).label('count')
    ).group_by('price_range').all()
    return price_distribution

if __name__ == "__main__":
    with app.app_context():
        db_init()
        demo_read()
        # agr_funcs()
        # groupby_stats()
        cat = having_func()
        products = case_when()