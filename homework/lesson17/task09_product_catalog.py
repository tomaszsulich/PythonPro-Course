from flask import render_template, request
from task08_product_model import app, Product


@app.route("/products")
def display_products() -> str:
    """
    Nadzoruje proces udostępniania danych produktów.
    
    Uwzględnia parametry wpływające na kolejność
    rekordów oraz sposób ich przedstawiania
    na stronie.
    """
    
    currency = request.args.get("currency", "PLN")
    sort_field = request.args.get("sort_field", "id")
    direction = request.args.get("direction", "asc")
    
    if sort_field == "name":
        column = Product.name
    elif sort_field == "company":
        column = Product.company
    elif sort_field == "price":
        column = Product.price
    else:
        column = Product.id
        
    if direction == "desc":
        products = Product.query.order_by(column.desc()).all()
    else:
        products = Product.query.order_by(column.asc()).all()
    
    return render_template(
        "products.html", 
        products = products,
        product_count = len(products),
        currency = currency,
    )
    
    
if __name__ == "__main__":
    app.run(debug=True)