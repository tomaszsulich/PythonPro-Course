import random
from decimal import Decimal

from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from shop.models import (Address, Category, Client,
                         Product, Transaction, TransactionItem)


PRODUCT_CATALOG = (
    (
        "Elektronika",
        (
            ("Laptop", "3499.99"),
            ("Smartfon", "2199.00"),
            ("Monitor", "899.99"),
            ("Klawiatura", "249.90"),
            ("Mysz bezprzewodowa", "129.99"),
        ),
    ),
    (
        "Książki",
        (
            ("Python. Wprowadzenie", "79.90"),
            ("Django w praktyce", "89.90"),
            ("Podstawy baz danych", "69.99"),
            ("Algorytmy i struktury danych", "99.00"),
            ("Czysty kod", "74.90"),
        ),
    ),
    (
        "Dom i kuchnia",
        (
            ("Czajnik elektryczny", "159.99"),
            ("Ekspres do kawy", "899.00"),
            ("Zestaw garnków", "429.90"),
            ("Blender kielichowy", "249.99"),
            ("Toster", "139.90"),
        ),
    ),
    (
        "Sport",
        (
            ("Mata do ćwiczeń", "89.99"),
            ("Hantle regulowane", "299.00"),
            ("Piłka treningowa", "69.90"),
            ("Rakieta tenisowa", "399.99"),
            ("Plecak sportowy", "179.90"),
        ),
    ),
    (
        "Artykuły spożywcze",
        (
            ("Ziemniaki 2 kg", "8.99"),
            ("Ryż 1 kg", "7.49"),
            ("Makaron 500 g", "5.99"),
            ("Oliwa z oliwek", "34.90"),
            ("Herbata liściasta", "18.99"),
        ),
    ),
    (
        "Biuro",
        (
            ("Notes A5", "19.99"),
            ("Długopis żelowy", "7.90"),
            ("Segregator", "14.99"),
            ("Kalkulator biurowy", "49.90"),
            ("Niszczarka dokumentów", "299.00"),
        ),
    ),
    (
        "Odzież",
        (
            ("Koszulka bawełniana", "59.99"),
            ("Bluza z kapturem", "179.90"),
            ("Spodnie jeansowe", "219.00"),
            ("Kurtka przeciwdeszczowa", "299.99"),
            ("Czapka zimowa", "69.90"),
        ),
    ),
    (
        "Gry i rozrywka",
        (
            ("Gra planszowa", "149.99"),
            ("Puzzle 1000 elementów", "54.90"),
            ("Karty do gry", "19.99"),
            ("Zestaw kości", "29.90"),
            ("Szachy drewniane", "119.00"),
        ),
    ),
)


class Command(BaseCommand):
    help = "Tworzy przykładowe dane biznesowe aplikacji shop."

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Usuwa istniejące dane biznesowe przed utworzeniem nowych.",
        )
        parser.add_argument(
            "--addresses",
            type=int,
            default=20,
            help="Liczba adresów do utworzenia. Domyślnie: 20.",
        )
        parser.add_argument(
            "--clients",
            type=int,
            default=20,
            help="Liczba klientów do utworzenia. Domyślnie: 20.",
        )
        parser.add_argument(
            "--categories",
            type=int,
            default=8,
            help="Liczba kategorii do utworzenia. Domyślnie: 8.",
        )
        parser.add_argument(
            "--products",
            type=int,
            default=40,
            help="Liczba produktów do utworzenia. Domyślnie: 40.",
        )
        parser.add_argument(
            "--transactions",
            type=int,
            default=30,
            help="Liczba transakcji do utworzenia. Domyślnie: 30.",
        )

    def handle(self, *args, **options):
        self._validate_options(options)

        fake = Faker("pl_PL")
        Faker.seed(42)
        random.seed(42)

        if options["clear"]:
            self._clear_data()

        selected_catalog = PRODUCT_CATALOG[:options["categories"]]

        addresses = self._create_addresses(
            fake,
            options["addresses"],
        )
        clients = self._create_clients(
            fake,
            addresses,
            options["clients"],
        )
        categories = self._create_categories(selected_catalog)
        products = self._create_products(
            selected_catalog,
            categories,
            options["products"],
        )
        transactions_count, items_count = self._create_transactions(
            clients,
            products,
            options["transactions"],
        )

        self.stdout.write(
            self.style.SUCCESS(
                "\nUtworzono przykładowe dane:\n"
                f"- adresy: {len(addresses)}\n"
                f"- klienci: {len(clients)}\n"
                f"- kategorie: {len(categories)}\n"
                f"- produkty: {len(products)}\n"
                f"- transakcje: {transactions_count}\n"
                f"- pozycje transakcji: {items_count}"
            )
        )

    @staticmethod
    def _validate_options(options):
        option_names = (
            "addresses",
            "clients",
            "categories",
            "products",
            "transactions",
        )

        for option_name in option_names:
            if options[option_name] < 0:
                raise CommandError(
                    f"Wartość --{option_name} nie może być ujemna."
                )

        if options["categories"] > len(PRODUCT_CATALOG):
            raise CommandError(
                "Maksymalna dostępna liczba kategorii wynosi "
                f"{len(PRODUCT_CATALOG)}."
            )

        selected_catalog = PRODUCT_CATALOG[:options["categories"]]
        available_products = sum(
            len(product_data)
            for _, product_data in selected_catalog
        )

        if options["products"] > available_products:
            raise CommandError(
                "Dla wybranej liczby kategorii dostępnych jest maksymalnie "
                f"{available_products} produktów."
            )

        if options["clients"] > 0 and options["addresses"] == 0:
            raise CommandError(
                "Do utworzenia klientów potrzebny jest co najmniej "
                "jeden adres."
            )

        if options["products"] > 0 and options["categories"] == 0:
            raise CommandError(
                "Do utworzenia produktów potrzebna jest co najmniej "
                "jedna kategoria."
            )

        if options["transactions"] > 0 and options["clients"] == 0:
            raise CommandError(
                "Do utworzenia transakcji potrzebny jest co najmniej "
                "jeden klient."
            )

        if options["transactions"] > 0 and options["products"] == 0:
            raise CommandError(
                "Do utworzenia transakcji potrzebny jest co najmniej "
                "jeden produkt."
            )

    def _clear_data(self):
        self.stdout.write("Usuwanie istniejących danych biznesowych...")

        TransactionItem.objects.all().delete()
        Transaction.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.all().delete()
        Client.objects.all().delete()
        Address.objects.all().delete()

        self.stdout.write(
            self.style.WARNING(
                "Dane biznesowe zostały usunięte. "
                "Konta użytkowników pozostawiono bez zmian."
            )
        )

    @staticmethod
    def _create_addresses(fake, count):
        return [
            Address.objects.create(
                street=fake.street_address(),
                city=fake.city(),
                postal_code=fake.postcode(),
            )
            for _ in range(count)
        ]

    @staticmethod
    def _create_clients(fake, addresses, count):
        return [
            Client.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                address=random.choice(addresses),
            )
            for _ in range(count)
        ]

    @staticmethod
    def _create_categories(catalog):
        return {
            category_name: Category.objects.create(name=category_name)
            for category_name, _ in catalog
        }

    @staticmethod
    def _create_products(catalog, categories, count):
        available_products = [
            (
                product_name,
                price,
                categories[category_name],
            )
            for category_name, product_data in catalog
            for product_name, price in product_data
        ]

        selected_products = available_products[:count]

        return [
            Product.objects.create(
                name=product_name,
                price=Decimal(price),
                category=category,
            )
            for product_name, price, category in selected_products
        ]

    @staticmethod
    def _create_transactions(clients, products, count):
        items_count = 0

        for _ in range(count):
            transaction = Transaction.objects.create(
                client=random.choice(clients),
            )

            selected_products = random.sample(
                products,
                k=random.randint(1, min(5, len(products))),
            )

            transaction_items = [
                TransactionItem(
                    transaction=transaction,
                    product=product,
                    quantity=random.randint(1, 5),
                )
                for product in selected_products
            ]

            TransactionItem.objects.bulk_create(transaction_items)
            items_count += len(transaction_items)

        return count, items_count