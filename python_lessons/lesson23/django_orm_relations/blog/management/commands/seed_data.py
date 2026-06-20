import random
import sys
from django.core.management.base import BaseCommand
from faker import Faker
from django_orm_relations.blog.models import Author, Post # Załóżmy, że mamy takie modele

class Command(BaseCommand):
    help = 'Seeds the database with sample data'
    
    def handle(self, *args, **options):
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