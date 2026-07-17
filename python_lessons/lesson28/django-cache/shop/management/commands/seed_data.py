import random
from decimal import Decimal

from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from shop.models import (Address, Category, Client, 
                         Product, Transaction, TransactionItem)


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

        addresses = self._create_addresses(
            fake,
            options["addresses"],
        )
        clients = self._create_clients(
            fake,
            addresses,
            options["clients"],
        )
        categories = self._create_categories(
            fake,
            options["categories"],
        )
        products = self._create_products(
            fake,
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
    def _create_categories(fake, count):
        return [
            Category.objects.create(
                name=f"{fake.unique.word().capitalize()} {index + 1}",
            )
            for index in range(count)
        ]

    @staticmethod
    def _create_products(fake, categories, count):
        products = []

        for index in range(count):
            price = Decimal(
                str(round(random.uniform(5, 500), 2))
            )

            products.append(
                Product.objects.create(
                    name=f"{fake.word().capitalize()} {index + 1}",
                    price=price,
                    category=random.choice(categories),
                )
            )

        return products

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