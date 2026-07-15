from rest_framework import viewsets
from .models import Product, Note, Author, Book
from rest_framework.decorators import api_view, permission_classes
from .serializers import ProductSerializer, NoteSerializer, AuthorSerializer, BookSerializer
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication
from django.http import JsonResponse


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # zadanie 10
    def get_queryset(self):
        queryset = Product.objects.all()
        # localhost: 8000/api/products/?min_price=100
        min_p = self.request.query_params.get('min_price')
        max_p = self.request.query_params.get('max_price')
        if min_p:
            queryset = queryset.filter(price__gte=min_p)
        if max_p:
            queryset = queryset.filter(price__lte=max_p)
        return queryset
    
    
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    
    
def set_name(request):
    # /api/set-name/?name=Anna
    name = request.GET.get('name', 'Gosc')
    
    response = JsonResponse({"message": f"Ciasteczko ustawione na {name}"})
    response.set_cookie('user_name', name, max_age=3600)
    return response


def hello(request):
    # Odczytanie ciasteczka z obiektu żądania
    name = request.COOKIES.get('user_name', 'Gość')
    
    return JsonResponse({"message": f"Witaj, {name}!"})


@api_view(['GET'])
def calculate(request):
    try:
        n1, n2 = float(request.GET['num1']), float(request.GET['num2'])
        op = request.GET['operation']
        ops = {
            'add': lambda x,y: x + y, # można też n1 + n2
            'subtract': lambda x,y: x - y,
            'multiply': lambda x,y: x * y,
            'divide': lambda x,y: x / y if y != 0 else 'Error'
        }
        # https://127.0.0.1:8000/api/calc/?num1=1&num2=10&operation=add
        return JsonResponse({"result": ops[op](n1, n2)})
    except Exception:
        return JsonResponse({"error": "Invalid input"}, status=400)
    

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

@api_view(["GET"])
@permission_classes([JWTStatelessUserAuthentication])
def my_api_view(request):
    ...