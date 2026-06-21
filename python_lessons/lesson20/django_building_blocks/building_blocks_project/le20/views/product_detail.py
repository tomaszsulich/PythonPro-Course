from django.shortcuts import render
    
def product_detail_view(request, product_id):
    products = [
        {"id": 1, "name": "Jabłka", "price": 3.50},
        {"id": 2, "name": "Banany", "price": 5.99},
        {"id": 3, "name": "Truskawki", "price": 12.00},
    ]
    
    product = next(
        (p for p in products if p["id"] == product_id),
        None
    )
    
    return render(request, "product_detail.html", {"product": product})