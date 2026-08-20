from decimal import Decimal, InvalidOperation

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Author, Book, Note, Product
from .serializers import (
    AuthorSerializer,
    BookSerializer,
    NoteSerializer,
    ProductSerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_params.get("max_price")

        try:
            if min_price is not None:
                queryset = queryset.filter(
                    price__gte=Decimal(min_price)
                )

            if max_price is not None:
                queryset = queryset.filter(
                    price__lte=Decimal(max_price)
                )
        except InvalidOperation:
            raise ValidationError(
                {
                    "price": (
                        "Parametry min_price i max_price "
                        "muszą być poprawnymi liczbami."
                    )
                }
            )

        return queryset


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by("-created_at")
    serializer_class = NoteSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(["GET"])
def set_name(request: Request):
    name = request.query_params.get("name", "")

    response = Response(
        {"message": f"Ustawiono imię: {name}"}
    )

    response.set_cookie(
        "user_name",
        name,
    )

    return response


@api_view(["GET"])
def hello(request: Request):
    name = request.COOKIES.get(
        "user_name",
        "Gość",
    )

    return Response(
        {"message": f"Witaj, {name}!"}
    )


@api_view(["GET"])
def calculate(request: Request):
    try:
        num1 = float(request.query_params.get("num1"))
        num2 = float(request.query_params.get("num2"))
    except (TypeError, ValueError):
        return Response(
            {
                "error": (
                    "Parametry num1 i num2 muszą być "
                    "poprawnymi liczbami."
                )
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    operation = request.query_params.get("operation")

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return Response(
                {
                    "error": (
                        "Dzielenie przez zero jest niedozwolone."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        result = num1 / num2
    else:
        return Response(
            {"error": "Niepoprawna operacja."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    return Response(
        {"result": result}
    )