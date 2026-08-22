from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import RegisterForm
from .models import Book, Genre, Reservation
from .services.reservation_service import ReservationError, reserve_copy


def catalog(request: HttpRequest) -> HttpResponse:
    books = Book.objects.prefetch_related("authors", "genres", "copies")
    query = request.GET.get("q", "").strip()
    genre = request.GET.get("genre", "").strip()
    available = request.GET.get("available") == "1"

    if query:
        books = books.filter(
            Q(title__icontains=query)
            | Q(authors__first_name__icontains=query)
            | Q(authors__last_name__icontains=query)
        )

    if genre:
        books = books.filter(genres__id=genre)

    if available:
        books = books.filter(copies__available=True)

    context = {
        "books": books.distinct(),
        "genres": Genre.objects.all(),
        "q": query,
        "selected_genre": genre,
        "available": available,
    }
    
    return render(request, "catalog.html", context)


def book_detail(request: HttpRequest, book_id: int) -> HttpResponse:
    book = get_object_or_404(
        Book.objects.prefetch_related("authors", "genres", "copies"),
        pk=book_id,
    )
    
    return render(request, "book_detail.html", {"book": book})


def register(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("library:catalog")

    form = RegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Konto zostało utworzone.")
        return redirect("library:catalog")

    return render(request, "register.html", {"form": form})


@login_required
def reserve(request: HttpRequest, copy_id: int) -> HttpResponse:
    if request.method != "POST":
        return redirect("library:catalog")

    try:
        reservation = reserve_copy(copy_id=copy_id, user=request.user)
    except ReservationError as exc:
        messages.error(request, str(exc))
    else:
        messages.success(
            request,
            f"Egzemplarz zarezerwowano do {reservation.reserved_until:%d.%m.%Y}.",
        )

    return redirect("library:my_reservations")


@login_required
def my_reservations(request: HttpRequest) -> HttpResponse:
    now = timezone.now()
    reservations = (
        Reservation.objects.filter(user=request.user)
        .select_related("copy__book")
    )

    return render(
        request,
        "my_reservations.html",
        {
            "current": reservations.filter(reserved_until__gte=now),
            "history": reservations.filter(reserved_until__lt=now),
        },
    )


def api_books(request: HttpRequest) -> JsonResponse:
    books = Book.objects.prefetch_related("authors", "genres")
    
    data = [
        {
            "id": book.id,
            "title": book.title,
            "authors": [str(author) for author in book.authors.all()],
            "genres": [genre.name for genre in book.genres.all()],
            "available_copies": book.available_copies_count,
        }
        for book in books
    ]
    
    return JsonResponse({"results": data})


def api_book_detail(request: HttpRequest, book_id: int) -> JsonResponse:
    book = get_object_or_404(
        Book.objects.prefetch_related("authors", "genres", "copies"),
        pk=book_id,
    )
    
    return JsonResponse(
        {
            "id": book.id,
            "title": book.title,
            "authors": [str(author) for author in book.authors.all()],
            "genres": [genre.name for genre in book.genres.all()],
            "copies": [
                {
                    "id": copy.id,
                    "inventory_code": copy.inventory_code,
                    "available": copy.available,
                }
                for copy in book.copies.all()
            ],
        }
    )


@login_required
def api_my_reservations(request: HttpRequest) -> JsonResponse:
    reservations = (
        Reservation.objects.filter(user=request.user)
        .select_related("copy__book")
    )
    
    return JsonResponse(
        {
            "results": [
                {
                    "id": item.id,
                    "book": item.copy.book.title,
                    "copy": item.copy.inventory_code,
                    "reserved_at": item.reserved_at.isoformat(),
                    "due_at": item.reserved_until.isoformat(),
                    "active": item.active,
                }
                for item in reservations
            ]
        }
    )