import random
from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Author, Post, Category, Tag

class Command(BaseCommand):
    help = 'Seeds the database with sample data'
    
    def add_arguments(self, parser):
        parser.add_argument("--clear",
                            "-c",
                            default=False,
                            action="store_true",
                            help="Delete existing data before seeding")
        parser.add_argument("--posts", 
                            "-p", 
                            default=50, 
                            type=int)
        
    def handle(self, *args, **options):
        if options["clear"]:
            self.stdout.write("Clearing data.")
            Post.objects.all().delete()
            Author.objects.all().delete()
            Category.objects.all().delete()
            Tag.objects.all().delete()

        self.stdout.write('Seeding data...')
        
        fake = Faker('pl_PL')
        
        tags = [Tag(name=fake.word()) for _ in range(20)]
        tags = Tag.objects.bulk_create(tags)
        
        # CATEGORY (dodane, bo wcześniej brakowało logiki)
        cat_s = ("Technologia", "Podróże", "Kulinaria", "Gry komputerowe")
        categories = [Category(name=c) for c in cat_s] # albo map
        categories = Category.objects.bulk_create(categories)
        
        self.stdout.write(
            self.style.SUCCESS(f"{len(categories)} categories created."))
        
        # AUTHORS
        authors = [
            Author(name=fake.name(), email=fake.email()) for _ in range(10)
        ]
        authors = Author.objects.bulk_create(authors)
        
        self.stdout.write(
            self.style.SUCCESS(f"{len(authors)} authors created."))
        
        
        def sample_tags():
            max_amount = min(5, len(tags))
            amount = random.randint(1, max_amount)
            return random.sample(tags, k=amount)
            
        # POSTS
        posts = [
            Post(title=fake.sentence(nb_words=6),
                 author=random.choice(authors),
                 category = random.choice(categories) if categories else None)
                 # tags = sample_tags())
            for _ in range(options["posts"])
        ]
            
        Post.objects.bulk_create(posts)
        
        self.stdout.write(self.style.SUCCESS(f"{len(posts)} posts created."))
        
        self.stdout.write(self.style.SUCCESS("Data seeding complete."))