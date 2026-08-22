from datetime import timedelta

from django.contrib.auth.models import User
from django.db import transaction
from django.utils import timezone

from library.models import BookCopy, Reservation


MAX_ACTIVE_RESERVATIONS = 5


class ReservationError(ValueError):
    pass


class CopyUnavailableError(ReservationError):
    pass


class BookAlreadyReservedError(ReservationError):
    pass


class ReservationLimitError(ReservationError):
    pass


@transaction.atomic
def reserve_copy(*, copy_id: int, user: User) -> Reservation:
    """Rezerwuje egzemplarz po sprawdzeniu limitów i dostępności."""
    user = User.objects.select_for_update().get(pk=user.pk)
    copy = (
        BookCopy.objects.select_for_update()
        .select_related("book")
        .get(pk=copy_id)
    )

    now = timezone.now()
    active_reservations = Reservation.objects.filter(
        user=user,
        reserved_until__gte=now,
    )

    if active_reservations.filter(copy__book=copy.book).exists():
        raise BookAlreadyReservedError(
            "Masz już aktywną rezerwację tej książki."
        )

    if active_reservations.count() >= MAX_ACTIVE_RESERVATIONS:
        raise ReservationLimitError(
            f"Możesz mieć maksymalnie {MAX_ACTIVE_RESERVATIONS} aktywnych rezerwacji."
        )

    active_copy_reservation = copy.reservations.filter(
        reserved_until__gte=now
    ).exists()

    if not copy.available or active_copy_reservation:
        raise CopyUnavailableError("Ten egzemplarz nie jest już dostępny.")

    reservation = Reservation.objects.create(
        user=user,
        copy=copy,
        reserved_at=now,
        reserved_until=now + timedelta(days=14),
    )

    copy.available = False
    copy.save(update_fields=["available"])
    return reservation