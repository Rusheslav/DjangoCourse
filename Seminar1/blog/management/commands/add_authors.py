from django.core.management import BaseCommand
from blog.models import Author


class Command(BaseCommand):
    help = 'Add 10 random authors'

    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            author = Author(name=f'Name{i}', surname=f'Surname{i}', email=f'mail{i}@mail.ru',
                            biography=f'One two three {i}', birthdate=f'190{i-1}-10-10')
            author.save()
            self.stdout.write(f'{author}')
