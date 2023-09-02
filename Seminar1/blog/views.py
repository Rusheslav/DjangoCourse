from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Author, Post


# Create your views here.
def author(request):
    result = ''
    for auth in Author.objects.all():
        result += str(auth) + '<br>'
    return HttpResponse(f'{result}')


def get_posts(request):
    result = ''
    for post in Post.objects.all():
        result += str(post) + '<br>'
    return HttpResponse(f'{result}')
