from django.db import models
from django.db.models import Manager
from django.urls import reverse


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    registration_date = models.DateField()

    objects = Manager()

    def __str__(self):
        return f'{self.name} - {self.email}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    amount = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add=True)

    objects = Manager()

    def get_absolute_url(self):
        return reverse('shop:product', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.name} - {self.price}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(decimal_places=2, max_digits=8)
    order_date = models.DateTimeField(auto_now_add=True)

    objects = Manager()

    def __str__(self):
        return f'{self.client} - {self.order_date} - {self.products} - {self.total_amount}'
