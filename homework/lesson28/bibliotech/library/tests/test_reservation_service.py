from datetime import timedelta

from django.contrib.auth.models import User
from django.test import TestCase

from library.models import Book, BookCopy
from library.services.reservation_service import (
    BookAlreadyReservedError,
    CopyUnavailableError,
    ReservationLimitError,
    reserve_copy,
)


class ReservationTests(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="ala", password="test12345")
        
        self.book = Book.objects.create(
            title="Test",
            description="Opis",
            publication_year=2026,
        )
        
        self.copy = BookCopy.objects.create(
            book=self.book,
            inventory_code="BT-001",
        )

    def test_reservation_lasts_14_days_and_marks_copy_unavailable(self) -> None:
        reservation = reserve_copy(copy_id=self.copy.id, user=self.user)
        self.copy.refresh_from_db()

        self.assertFalse(self.copy.available)
        
        self.assertAlmostEqual(
            reservation.reserved_until,
            reservation.reserved_at + timedelta(days=14),
            delta=timedelta(seconds=1),
        )

    def test_unavailable_copy_cannot_be_reserved_again(self) -> None:
        reserve_copy(copy_id=self.copy.id, user=self.user)
        other = User.objects.create_user(username="ola", password="test12345")

        with self.assertRaises(CopyUnavailableError):
            reserve_copy(copy_id=self.copy.id, user=other)

    def test_user_cannot_reserve_two_copies_of_the_same_book(self) -> None:
        second_copy = BookCopy.objects.create(
            book=self.book,
            inventory_code="BT-002",
        )
        
        reserve_copy(copy_id=self.copy.id, user=self.user)

        with self.assertRaises(BookAlreadyReservedError):
            reserve_copy(copy_id=second_copy.id, user=self.user)

    def test_user_cannot_exceed_five_active_reservations(self) -> None:
        for index in range(5):
            book = Book.objects.create(
                title=f"Książka {index}",
                description="Opis",
                publication_year=2026,
            )
            
            copy = BookCopy.objects.create(
                book=book,
                inventory_code=f"BT-LIMIT-{index}",
            )
            
            reserve_copy(copy_id=copy.id, user=self.user)

        sixth_book = Book.objects.create(
            title="Szósta książka",
            description="Opis",
            publication_year=2026,
        )
        
        sixth_copy = BookCopy.objects.create(
            book=sixth_book,
            inventory_code="BT-LIMIT-6",
        )

        with self.assertRaises(ReservationLimitError):
            reserve_copy(copy_id=sixth_copy.id, user=self.user)
