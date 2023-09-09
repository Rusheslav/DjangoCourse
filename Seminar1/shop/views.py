from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

from . import forms
from shop.models import Client, Product, Order
from django.views.generic import TemplateView, CreateView, DetailView


def get_clients(request):
    results = Client.objects.all()
    return HttpResponse(str(result) + '<br>' for result in results)


def get_products(request):
    products = Product.objects.all()
    return HttpResponse(str(product) + '<br>' for product in products)


def get_orders(request):
    results = Order.objects.all()
    return HttpResponse(str(result) + '<br>' for result in results)


class ClientOrdersView(TemplateView):
    template_name = 'shop/client_orders.html'

    def get_context_data(self, **kwargs):
        client = Client.objects.filter(pk=self.kwargs['pk']).first()
        orders = Order.objects.filter(client=client).prefetch_related('products')
        context = super().get_context_data()
        context['orders'] = orders
        return context


class AddProduct(CreateView):
    model = Product
    template_name = 'shop/add_product.html'
    form_class = forms.AddProductForm  # Specify the form class here

    def form_valid(self, form):
        image = form.cleaned_data['image']
        response = super().form_valid(form)
        fs = FileSystemStorage()
        fs.save(image.name, image)
        return response


class ProductPage(DetailView):
    model = Product
    template_name = 'shop/product.html'
