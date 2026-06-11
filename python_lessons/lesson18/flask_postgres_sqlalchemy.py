from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from auth import USER, PWD, DATABASE

app = Flask(__name__)

# Konfiguracja połączenia z bazą danych
# Format: postgresql://uzytkownik:haslo@host:port/nazwa_bazy
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{USER}:{PWD}@localhost/{DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Wyłączenie niepotrzebnej funkcji śledzenia

# Inicjalizacja obiektu SQLAlchemy
db = SQLAlchemy(app)

# Definicja modelu (tabeli) za pomocą klasy
# Dziedziczymy po db.Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Metoda __repr__ definiuje, jak obiekt będzie wyglądał po wydrukowaniu
    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/')
def index():
    # Pobieranie wszystkich użytkowników z bazy
    # User.query.all() to odpowiednik "SELECT * FROM user;"
    users = User.query.all()
    return render_template('index.html', users=users)

def db_init():
    with db.session() as sess:
        sess.create_all()


if __name__ == "__main__":
    app.run()