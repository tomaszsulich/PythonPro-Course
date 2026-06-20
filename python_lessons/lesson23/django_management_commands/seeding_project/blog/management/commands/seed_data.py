import random
import sys
from django.core.management.base import BaseCommand
from faker import Faker
from ...models import Author, Post # Załóżmy, że mamy takie modele

class Command(BaseCommand):
    help = 'Seeds the database with sample data'
    
    def add_arguments(self, parser):
        parser.add_argument("--clear",
                            default=False,
                            action="store_true",
                            help="Delete existing data before seeding")
        
    def handle(self, *args, **options):
        if options["clear"]:
            self.stdout.write("Clearing data.")
            Author.objects.all().delete()
            Post.objects.all().delete()
        self.stdout.write('Seeding data...')
        # Inicjalizujemy Faker
        fake = Faker('pl_PL') # Używamy polskiego wariantu
        # Stwórzmy 10 autorów
        authors = [Author(name=fake.name(), email=fake.email())
                   for _ in range(10)]
        authors = Author.objects.bulk_create(authors)
        self.stdout.write(self.style.SUCCESS(f'{len(authors)} authors created.'))
        # Stwórzmy 50 postów
        posts = [Post(title=fake.sentence(nb_words=6),
                      author=random.choice(authors)) # Losowy autor z listy
            for _ in range(50)]
        Post.objects.bulk_create(posts)
        
        self.stdout.write(self.style.SUCCESS(f'{len(posts)} posts created.'))
        self.stdout.write(self.style.SUCCESS('Data seeding complete.'))