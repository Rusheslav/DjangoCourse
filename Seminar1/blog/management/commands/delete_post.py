from django.core.management import BaseCommand
from blog.models import Post


class Command(BaseCommand):
    help = 'Update post title by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Post pk')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        post = Post.objects.filter(pk=pk).first()
        post.delete()
        self.stdout.write(f'Post deleted: {post}.')
