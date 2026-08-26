import random
import threading
from decimal import Decimal


THREAD_COUNT = 5
MIN_AMOUNT = 10
MAX_AMOUNT = 100
INITIAL_BALANCE = Decimal("200.37")


# Polskie nazewnictwo klasy, atrybutu i metod zachowano zgodnie z treścią zadania.
class KontoBankowe:
    def __init__(self, saldo: Decimal) -> None:
        self.saldo = saldo
        self._lock = threading.Lock()

    def wplac(self, kwota: int) -> None:
        with self._lock:
            self.saldo += Decimal(kwota)

    def wyplac(self, kwota: int) -> bool:
        with self._lock:
            if self.saldo < Decimal(kwota):
                return False

            self.saldo -= Decimal(kwota)
            return True


def wykonaj_wplate(konto: KontoBankowe, kwota: int) -> None:
    konto.wplac(kwota)
    print(f"Wpłacono: {kwota} zł")


def wykonaj_wyplate(konto: KontoBankowe, kwota: int, successful_withdrawals: list[int]) -> None:
    if konto.wyplac(kwota):
        successful_withdrawals.append(kwota)
        print(f"Wypłacono: {kwota} zł")
    else:
        print(f"Odrzucono wypłatę: {kwota} zł")


def main() -> None:
    konto = KontoBankowe(INITIAL_BALANCE)
    successful_withdawals: list[int] = []

    deposit_amounts = [
        random.randint(MIN_AMOUNT, MAX_AMOUNT)
        for _ in range(THREAD_COUNT)
    ]

    withdrawal_amounts = [
        random.randint(MIN_AMOUNT, MAX_AMOUNT)
        for _ in range(THREAD_COUNT)
    ]

    threads = []

    for deposit_amount, withdrawal_amount in zip(
        deposit_amounts,
        withdrawal_amounts,
    ):
        deposit_thread = threading.Thread(
            target=wykonaj_wplate,
            args=(konto, deposit_amount),
        )

        withdrawal_thread = threading.Thread(
            target=wykonaj_wyplate,
            args=(konto, withdrawal_amount, successful_withdawals),
        )

        threads.extend([deposit_thread, withdrawal_thread])

    random.shuffle(threads)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    expected_balance = (
        INITIAL_BALANCE
        + Decimal(sum(deposit_amounts))
        - Decimal(sum(successful_withdawals))
    )

    print(f"Saldo początkowe: {INITIAL_BALANCE:.2f} zł")
    print(f"Saldo oczekiwane: {expected_balance:.2f} zł")
    print(f"Saldo końcowe: {konto.saldo:.2f} zł")
    print(f"Weryfikacja: {konto.saldo == expected_balance}")


if __name__ == "__main__":
    main()