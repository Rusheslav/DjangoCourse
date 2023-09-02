from random import randint, shuffle
from django.core.management import BaseCommand
from shop.models import Product, Client, Order


class Command(BaseCommand):
    help = 'Add new orders'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='Number of products added')

    def handle(self, *args, **kwargs):
        number = kwargs.get('number')
        products = Product.objects.all()
        clients = Client.objects.all()
        for i in range(number):
            cart = list(products)
            shuffle(cart)
            cart = cart[:randint(1, len(products))]
            print(cart)
            order = Order(client=clients[randint(0, len(clients) - 1)],
                          # products=cart,
                          total_amount=sum([product.price for product in cart]),
                          order_date=f'{randint(1900, 2023)}-{randint(1, 12)}-{randint(1, 28)}')
            order.save()
            order.products.set(cart)
            self.stdout.write(f'Order placed: {order}.')
