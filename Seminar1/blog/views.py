import logging

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, CreateView
from blog import forms
from blog.models import Author, Post, Comment

logger = logging.getLogger(__name__)


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
        context['title'] = 'Статьи автора'
        context['results'] = results
        return context


class DetailPost(DetailView):
    model = Post
    template_name = 'blog/detailed_post.html'
    # form_class = forms.AddCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        post = Post.objects.filter(pk=self.kwargs['pk']).first()
        comments = Comment.objects.filter(post=post).all()
        context['comments'] = comments
        context['form'] = forms.AddCommentForm()
        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj

    def post(self, request, *args, **kwargs):
        form = forms.AddCommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            if not author:
                author = 'Анонимус'
            content = form.cleaned_data['content']
            post = Post.objects.filter(pk=self.kwargs['pk']).first()
            comment = Comment(author=author, content=content, post=post)
            comment.save()
            logger.info(f'Получили {author = }, {content = }.')
        return self.get(request, args, kwargs)


class AddAuthor(CreateView):
    model = Author
    template_name = 'blog/add_author.html'
    form_class = forms.AddAuthorForm


class AuthorPage(DetailView):
    model = Author
    template_name = 'blog/author.html'


class AddPost(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    form_class = forms.AddPostForm
