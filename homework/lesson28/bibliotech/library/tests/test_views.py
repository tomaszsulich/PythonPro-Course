from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from library.models import Book, Genre


class ViewTests(TestCase):
    def test_catalog_is_public(self) -> None:
        response = self.client.get(reverse("library:catalog"))
        self.assertEqual(response.status_code, 200)

    def test_book_detail_is_public(self) -> None:
        book = Book.objects.create(
            title="Test",
            description="Opis",
            publication_year=2026,
        )
        
        response = self.client.get(reverse("library:book_detail", args=[book.id]))
        self.assertEqual(response.status_code, 200)

    def test_reservations_panel_requires_login(self) -> None:
        response = self.client.get(reverse("library:my_reservations"))
        self.assertEqual(response.status_code, 302)

    def test_books_api_returns_success(self) -> None:
        response = self.client.get(reverse("library:api_books"))
        self.assertEqual(response.status_code, 200)

    def test_login_redirects_authenticated_user_to_catalog(self) -> None:
        user = User.objects.create_user(
            username="ala",
            password="test12345",
        )
        
        self.client.force_login(user)
        response = self.client.get(reverse("login"))
        self.assertRedirects(response, reverse("library:catalog"))

    def test_catalog_can_filter_by_genre(self) -> None:
        genre = Genre.objects.create(name="Kryminał")
        
        book = Book.objects.create(
            title="Nocny dyżur",
            description="Opis",
            publication_year=2026,
        )
        
        book.genres.add(genre)

        response = self.client.get(
            reverse("library:catalog"),
            {"genre": genre.id},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nocny dyżur")
