import requests
from django.core.management import BaseCommand

from jewelry import settings
from order.models import Order
from order.hooks import order_log


class Command(BaseCommand):
    def handle(self, *args, **options):
        orders = (
            Order.objects
            .filter(products__product__name="ANELLO ROSONE DI COLLEMAGGIO bombato e pietra")
            .order_by("-id")
            .all()
        )
        for order in orders:
            if order.products.exists():
                for product in order.products.all():
                    print("DEBUG", product.ring_size)
                order_log(order)

        else:
            print("No orders found with products.")
            return
        
