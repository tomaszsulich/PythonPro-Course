import time

from flask import Flask
from one_to_many import Product, db # KLUCZOWE: Twoje modele + db
from sqlalchemy import event
from sqlalchemy.orm import joinedload

app = Flask(__name__)

# jeśli nie konfigurujesz w one_to_many.py w tym samym procesie,
# to musisz powtórzyć config albo importować app z one_to_many
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///one_to_many.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app) # ważne przy rozdzieleniu plików


# DEBUGGING: Licznik zapytań SQL
query_count = 0

with app.app_context():
    @event.listens_for(db.engine, "before_cursor_execute")
    def count_queries(conn, cursor, statement, parameters, context, executemany):
        global query_count
        query_count += 1
        
        
@app.route("/demo-n-plus-1")
def demo_n_plus_1():
    """Demonstracja problemu N+1."""
    global query_count
    
    results = []
    
    # ❌ ZŁY SPOSÓB - N+1
    query_count = 0
    start = time.time()
    
    products = Product.query.all() # 1 zapytanie
    
    bad_result = []
    for p in products:
        bad_result.append(f"{p.name} - {p.category.name}") # N zapytań
        
    bad_time = time.time() - start
    bad_queries = query_count
    
    # ✅ DOBRY SPOSÓB - eager loading
    query_count = 0
    start = time.time()
    
    products = Product.query.options(joinedload(Product.category)).all()
    
    good_result = []
    for p in products:
        good_result.append(f"{p.name} - {p.category.name}") # 0 dodatkowych zapytań
        
    good_time = time.time() - start
    good_queries = query_count
    
    return f"""
    <h2>Porównanie wydajności</h2>
    <table border="1" cellpadding="10">
        <tr>
            <th>Metoda</th>
            <th>Zapytań SQL</th>
            <th>Czas</th>
        </tr>
        <tr style="background: #ffcccc">
            <td>❌ N+1 problem</td>
            <td>{bad_queries}</td>
            <td>{bad_time * 1000:.2f} ms</td>
        </tr>
        <tr style="background: #ccffcc">
            <td>✅ joinedload</td>
            <td>{good_queries}</td>
            <td>{good_time * 1000:.2f} ms</td>
        </tr>
    </table>
    <p>Różnica: {bad_queries / good_queries if good_queries else 0:.0f}x mniej zapytań</p>
    """
    
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)