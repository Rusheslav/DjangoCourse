from random import randint
from django.core.management import BaseCommand
from shop.models import Client


class Command(BaseCommand):
    help = 'Add new clients'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='Number of clients added')

    def handle(self, *args, **kwargs):
        number = kwargs.get('number')
        for i in range(number):
            client = Client(name=f'Name{i}',
                            email=f'mail{i}@mail.ru',
                            phone=f'{randint(111, 999)} - {randint(1111, 9999)}',
                            address=f'Moscow, Mokhovaya str., {randint(1, 99)}, {randint(1, 150)}',
                            registration_date=f'{randint(1900, 2023)}-{randint(1, 12)}-{randint(1, 28)}')
            client.save()
            self.stdout.write(f'Client created: {client}.')
