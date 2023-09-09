from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('clients', views.get_clients, name='clients'),
    path('products', views.get_products, name='products'),
    path('orders', views.get_orders, name='orders'),
    path('client_orders/<int:pk>', views.ClientOrdersView.as_view(), name='client_orders'),
    path('product/<int:pk>', views.ProductPage.as_view(), name='product'),
    path('add_product', views.AddProduct.as_view(), name='add_product'),
]
