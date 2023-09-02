from django.core.management import BaseCommand
from blog.models import Author, Post, Category
from random import randint


class Command(BaseCommand):
    help = 'Add 10 random posts'

    def handle(self, *args, **kwargs):
        authors = Author.objects.all()
        categories = Category.objects.all()
        for i in range(1, 11):
            post = Post(title=f'Title{i}', content=f'Hgslkgnd asdglsdng lksnd{i}', published_date=f'190{i - 1}-10-10',
                        author=authors[0], category=categories[0], views=f'10{i}',
                        published=f'{(True, False)[randint(0, 1)]}')
            post.save()
            self.stdout.write(f'{post}')
