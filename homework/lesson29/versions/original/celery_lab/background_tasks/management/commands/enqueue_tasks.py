import random

from django.core.management.base import BaseCommand

from background_tasks.tasks import multiply


class Command(BaseCommand):
    help = "Dodaje do kolejki 50 zadań mnożenia z losowymi liczbami."
    
    def handle(self, *args, **options) -> None:
        for _ in range(50):
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            multiply.delay(a, b)
            
        self.stdout.write(
            self.style.SUCCESS("Pomyślnie dodano 50 zadań do kolejki.")
        )