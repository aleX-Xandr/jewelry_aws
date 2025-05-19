import requests
from django.core.management import BaseCommand

from jewelry import settings
from order.models import Order
from order.hooks import order_log


class Command(BaseCommand):
    def handle(self, *args, **options):
        orders = Order.objects.order_by("-id").all()
        for order in orders:
            if order.products.exists():
                order_log(order)
                break

        else:
            print("No orders found with products.")
            return
        
