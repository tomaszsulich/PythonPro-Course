from django.contrib import admin

from .models import Author, Book, BookCopy, Genre, Reservation


class BookCopyInline(admin.TabularInline):
    model = BookCopy
    extra = 1


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")
    search_fields = ("first_name", "last_name")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "publication_year")
    search_fields = ("title", "authors__first_name", "authors__last_name")
    list_filter = ("genres",)
    inlines = (BookCopyInline,)


@admin.register(BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    list_display = ("inventory_code", "book", "available")
    search_fields = ("inventory_code", "book__title")
    list_filter = ("available",)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("user", "copy", "reserved_at", "reserved_until")
    
    search_fields = (
        "user__username",
        "copy__inventory_code",
        "copy__book__title",
    )
    
    list_filter = ("reserved_at", "reserved_until")