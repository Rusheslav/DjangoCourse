from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('authors', views.author, name='authors'),
    path('posts', views.get_posts, name='posts'),
    path('posts/<str:surname>', views.PostsByAuthor.as_view(), name='posts_by_author'),
    path('post/<int:pk>', views.DetailPost.as_view(), name='detail_post'),
    path('add_author', views.AddAuthor.as_view(), name='add_author'),
    path('author/<int:pk>', views.AuthorPage.as_view(), name='author'),
    path('add_post', views.AddPost.as_view(), name='add_post'),
]
