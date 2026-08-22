from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Autor"
        verbose_name_plural = "Autorzy"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Gatunek"
        verbose_name_plural = "Gatunki"

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name="books")
    genres = models.ManyToManyField(Genre, related_name="books")
    description = models.TextField()
    publication_year = models.PositiveIntegerField()
    cover = models.ImageField(upload_to="covers/", blank=True, null=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Książka"
        verbose_name_plural = "Książki"

    def __str__(self) -> str:
        return self.title

    @property
    def available_copies_count(self) -> int:
        return self.copies.filter(available=True).count()


class BookCopy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="copies")
    inventory_code = models.CharField(max_length=50, unique=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ["inventory_code"]
        verbose_name = "Egzemplarz"
        verbose_name_plural = "Egzemplarze"

    def __str__(self) -> str:
        return f"{self.book.title} ({self.inventory_code})"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")
    
    copy = models.ForeignKey(
        BookCopy,
        on_delete=models.PROTECT,
        related_name="reservations",
    )
    
    reserved_at = models.DateTimeField(default=timezone.now)
    reserved_until = models.DateTimeField()

    class Meta:
        ordering = ["-reserved_at"]
        verbose_name = "Rezerwacja"
        verbose_name_plural = "Rezerwacje"

    def save(self, *args, **kwargs) -> None:
        if not self.reserved_until:
            self.reserved_until = self.reserved_at + timedelta(days=14)
        super().save(*args, **kwargs)

    @property
    def active(self) -> bool:
        return self.reserved_until >= timezone.now()

    def __str__(self) -> str:
        return f"{self.user.username} — {self.copy}"