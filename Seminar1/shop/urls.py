from django.urls import path
from . import views

urlpatterns = [
    path('clients', views.get_clients, name='clients'),
    path('products', views.get_products, name='products'),
    path('orders', views.get_orders, name='orders'),
    path('client_orders/<int:pk>', views.ClientOrdersView.as_view(), name='client_orders')
]
