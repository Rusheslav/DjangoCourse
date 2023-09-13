from django.contrib import admin
from .models import Author, Category, Post, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'biography', 'birthdate']
    search_fields = ['surname']
    search_help_text = 'Поиск по фамилии'


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date', 'author', 'category', 'published']
    readonly_fields = ['views']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'published_date', 'author', 'post']


# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
