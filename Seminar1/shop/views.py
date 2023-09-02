from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Client, Product, Order


def get_clients(request):
    results = Client.objects.all()
    return HttpResponse(str(result) + '<br>' for result in results)


def get_products(request):
    products = Product.objects.all()
    return HttpResponse(str(product) + '<br>' for product in products)


def get_orders(request):
    results = Order.objects.all()
    return HttpResponse(str(result) + '<br>' for result in results)
