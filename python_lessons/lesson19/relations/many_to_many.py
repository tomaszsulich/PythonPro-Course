from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///many_to_many.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

# =========================
# TABELA ŁĄCZĄCA M:N
# =========================
product_tags = db.Table(
    "product_tags",
    db.Column("product_id", db.Integer, db.ForeignKey("products.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"), primary_key=True),
    db.Column("added_at", db.DateTime, default=db.func.now())
)

# =========================
# MODELE
# =========================


class Category(db.Model):
    __tablename__ = "categories"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True, nullable = False)
    

class Tag(db.Model):
    __tablename__ = "tags"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique = True, nullable = False)
    color = db.Column(db.String(7), default = "#6c757d")
    
    def __repr__(self):
        return f"<Tag {self.name}>"
    

class Product(db.Model):
    __tablename__ = "products"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True, nullable = False)
    price = db.Column(db.Numeric(10, 2), nullable = False)
    category = db.relationship("Category", backref = "products")
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable = False)
    
    tags = db.relationship(
        "Tag",
        secondary = product_tags,
        lazy = "subquery",
        backref = db.backref("products", lazy = True),
    )
    
    def __repr__(self):
        return f"<Product {self.name}>"
    

# =========================
# INIT DB
# =========================


def db_init():
    with app.app_context():
        db.create_all()
        
        if not Category.query.first():
            electronics = Category(name="Electronics")
            db.session.add(electronics)
            
            laptop = Product(name="Laptop Dell", price=4999.00, category_id=1)
            phone = Product(name="iPhone", price=3999.00, category_id=1)
            
            promo = Tag(name="Promocja", color="#dc3545")
            nowosc = Tag(name="Nowość", color="#28a745")
            bestseller = Tag(name="Bestseller", color="#ffc107")
            
            db.session.add_all([laptop, phone, promo, nowosc, bestseller])
            db.session.commit()
            
            laptop.tags.append(promo)
            laptop.tags.append(bestseller)
            phone.tags.append(nowosc)
            db.session.commit()
            
            
@app.route("/")
def index():
    
    laptop = Product.query.filter_by(name="Laptop Dell").first()
    
    output = f"Produkt: {laptop.name}\n\nTagi:\n"
    for tag in laptop.tags:
        output += f"- {tag.name}\n"
        
    promo_products = Product.query.filter(Product.tags.any(name="Promocja")).all()
    
    output += "\n Produkty z 'Promocja':\n"
    for p in promo_products:
        output += f"- {p.name}\n"
        
    return f"<pre>{output}</pre>"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        db_init()
        
    app.run(debug=True, use_reloader=False)
