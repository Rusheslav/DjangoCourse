from django.db import models
from django.db.models import Manager
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthdate = models.DateField()

    objects = Manager()

    def get_absolute_url(self):
        return reverse('blog:author', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.name} {self.surname}'


class Category(models.Model):
    name = models.CharField(max_length=100)
    objects = Manager()

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    views = models.IntegerField(default=0)
    published = models.BooleanField(default=False)

    objects = Manager()

    def get_absolute_url(self):
        return reverse('blog:detail_post', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20, default='Анонимус')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    objects = Manager()

    def __str__(self):
        return f'{self.author} {self.content}'
