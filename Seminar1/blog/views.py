from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView

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


class PostsByAuthor(TemplateView):
    template_name = 'blog/posts.html'

    def get_context_data(self, **kwargs):
        auth = Author.objects.filter(surname=self.kwargs['surname']).first()
        results = [post for post in Post.objects.filter(author=auth)]
        context = super().get_context_data()
        context['title'] = 'Статьм автора'
        context['results'] = results
        return context


class DetailPost(DetailView):
    model = Post
    template_name = 'blog/detailed_post.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj
