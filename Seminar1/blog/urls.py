from django.urls import path
from . import views

urlpatterns = [
    path('authors', views.author, name='authors'),
    path('posts', views.get_posts, name='posts'),
]
