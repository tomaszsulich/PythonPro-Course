import random

from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Category, Post, Tag


class Command(BaseCommand):
    help = "Seeds the blog database with categories, tags, and posts"

    def handle(self, *args, **kwargs) -> None:
        self.stdout.write("Removing existing blog data...")

        Post.objects.all().delete()
        Category.objects.all().delete()
        Tag.objects.all().delete()

        fake = Faker("pl_PL")

        category_names = [
            "Technologia",
            "Podróże",
            "Kulinaria",
            "Sport",
            "Kultura",
            "Nauka",
            "Zdrowie",
            "Rozrywka",
        ]

        tag_names = [
            "Python",
            "Django",
            "Programowanie",
            "Poradnik",
            "Nowości",
            "Inspiracje",
            "Lifestyle",
            "Recenzja",
            "Trendy",
            "Praktyka",
        ]

        categories = [
            Category.objects.create(name=name)
            for name in category_names
        ]

        tags = [
            Tag.objects.create(name=name)
            for name in tag_names
        ]

        self.stdout.write(
            self.style.SUCCESS(
                f"{len(categories)} categories created."
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"{len(tags)} tags created."
            )
        )

        posts = []

        for _ in range(100):
            post = Post.objects.create(
                title=fake.sentence(nb_words=6),
                content="\n\n".join(
                    fake.paragraphs(nb=5)
                ),
                category=random.choice(categories),
            )

            selected_tags = random.sample(
                tags,
                k=random.randint(1, 5),
            )

            post.tags.set(selected_tags)
            posts.append(post)

        self.stdout.write(
            self.style.SUCCESS(
                f"{len(posts)} posts created."
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Blog data seeding complete."
            )
        )