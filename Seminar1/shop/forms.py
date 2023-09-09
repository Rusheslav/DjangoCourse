from django import forms
from . import models


class AddProductForm(forms.ModelForm):
    image = forms.ImageField(required=True)

    class Meta:
        model = models.Product
        fields = ['name', 'description', 'price', 'amount', 'image']
