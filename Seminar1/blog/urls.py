from django.urls import path
from . import views

urlpatterns = [
    path('authors', views.author, name='authors'),
    path('posts', views.get_posts, name='posts'),
    path('posts/<str:surname>', views.PostsByAuthor.as_view(), name='posts_by_author'),
    path('post/<int:pk>', views.DetailPost.as_view(), name='detail_post')
]
