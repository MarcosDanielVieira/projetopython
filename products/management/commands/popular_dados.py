from django.core.management.base import BaseCommand
from faker import Faker
import random
from products.models import Brand, Category, Product


class Command(BaseCommand):
    help = "Popula o banco com dados falsos"

    def handle(self, *args, **kwargs):
        fake = Faker('pt_BR')

        for _ in range(10):
            Brand.objects.create(
                name=fake.company(),
                is_active=random.choice([True, False]),
                description=fake.text(max_nb_chars=100)
            )

        for _ in range(5):
            Category.objects.create(
                name=fake.word().capitalize(),
                is_active=random.choice([True, False]),
                description=fake.text(max_nb_chars=100)
            )

        brands = list(Brand.objects.all())
        categories = list(Category.objects.all())

        for _ in range(50):
            Product.objects.create(
                title=fake.catch_phrase(),
                brand=random.choice(brands),
                category=random.choice(categories),
                price=round(random.uniform(10.0, 1000.0), 2),
                is_active=random.choice([True, False]),
                description=fake.text(max_nb_chars=200)
            )

        self.stdout.write(self.style.SUCCESS(
            "Dados faker gerados com sucesso!"))
