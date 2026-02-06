from django.core.management.base import BaseCommand
from faker import Faker
from products.models import Category, Product
from orders.models import Store, Inventory
import random

class Command(BaseCommand):
    help = 'Seed test data for Aforro'

    def handle(self, *args, **options):
        fake = Faker()
        print('🌱 Seeding data...')

        # Clear old data
        Category.objects.all().delete()
        Product.objects.all().delete()
        Store.objects.all().delete()
        Inventory.objects.all().delete()

        # 10 Categories
        categories = []
        for _ in range(10):
            cat = Category.objects.create(name=fake.word().capitalize())
            categories.append(cat)

        # 50 Products
        for _ in range(50):
            Product.objects.create(
                title=fake.sentence(nb_words=3)[:-1],
                price=round(random.uniform(10, 1000), 2),
                category=random.choice(categories)
            )

        # 5 Stores
        stores = []
        for _ in range(5):
            store = Store.objects.create(
                name=fake.company(), 
                location=fake.city()
            )
            stores.append(store)

        # Inventory
        products = list(Product.objects.all())
        for store in stores:
            for product in random.sample(products, 20):
                Inventory.objects.create(
                    store=store, 
                    product=product,
                    quantity=random.randint(0, 100)
                )

        print(f'✅ SUCCESS: {Product.objects.count()} products, {Store.objects.count()} stores!')
