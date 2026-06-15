from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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
        
        db.session.add(elektronika)
        db.session.flush() # żeby mieć elektronika.id
        
        laptop = Product(name = "Laptop Dell", price = 3500, category = elektronika)
        laptop2 = Product(name = "MacBook", price = 6000, category_id = elektronika.id)
        
        db.session.add_all([laptop, laptop2])
        db.session.commit()

     
def demo_read():
    kategoria = Category.query.filter_by(name="Elektronika").first()
    
    print(f"Kategoria: {kategoria.name}")
    for p in kategoria.products:
        print(f" - {p.name}: {p.price} PLN")
        
    produkt = Product.query.first()
    print(f"{produkt.name} jest w kategorii: {produkt.category.name}")
    

if __name__ == "__main__":
    with app.app_context():
        db_init()
        demo_read()