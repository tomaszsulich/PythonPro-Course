from django.shortcuts import render

def about_view(request):
    context = {
        "user_name": "Anna",
        "products": [
            {"name": "Jabłka", "price": 3.50},
            {"name": "Banany", "price": 5.99},
            {"name": "Truskawki", "price": 12.00},
        ],
    }
    return render(request, "about.html", context)