from django import forms
from blog import models


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ['name', 'surname', 'email', 'biography', 'birthdate']


class AddPostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'content', 'author', 'category']


class AddCommentForm(forms.ModelForm):
    author = forms.CharField(max_length=20, required=False)

    class Meta:
        model = models.Comment
        fields = ['author', 'content']
