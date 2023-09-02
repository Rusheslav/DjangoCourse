from django.core.management import BaseCommand
from blog.models import Author, Post, Category
from random import randint


class Command(BaseCommand):
    help = 'Create post'

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Post title')
        parser.add_argument('content', type=str, help='Post content')
        parser.add_argument('published_date', type=str, help='Post date')
        parser.add_argument('author', type=int, help='Post author')
        parser.add_argument('category', type=int, help='Post category')
        parser.add_argument('views', type=str, help='Number of post views')
        parser.add_argument('published', type=int, help='Post status')

    def handle(self, *args, **kwargs):
        authors = Author.objects.all()
        categories = Category.objects.all()
        title = kwargs.get('title')
        content = kwargs.get('content')
        published_date = kwargs.get('published_date')
        author = kwargs.get('author')
        category = kwargs.get('category')
        views = kwargs.get('views')
        published = kwargs.get('published')

        print(author, category, views)

        post = Post(title=title, content=content, published_date=published_date,
                    author=authors[author], category=categories[category], views=views,
                    published=published)
        post.save()
        self.stdout.write(f'Post {post} added.')
