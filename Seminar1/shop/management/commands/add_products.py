from random import randint
from django.core.management import BaseCommand
from shop.models import Product


class Command(BaseCommand):
    help = 'Add new products'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='Number of products added')

    def handle(self, *args, **kwargs):
        number = kwargs.get('number')
        for i in range(number):
            product = Product(name=f'Name{i}',
                              description=f'Burarum {i} hastler',
                              price=f'{randint(11, 9999)}',
                              amount=f'{randint(1, 99)}',
                              added_date=f'{randint(1900, 2023)}-{randint(1, 12)}-{randint(1, 28)}')
            product.save()
            self.stdout.write(f'Post title corrected: {product}.')
