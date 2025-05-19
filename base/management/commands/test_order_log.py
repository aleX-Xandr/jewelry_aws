import requests
from django.core.management import BaseCommand

from jewelry import settings
from order.models import Order
from order.hooks import order_log


class Command(BaseCommand):
    def handle(self, *args, **options):
        order = Order.objects.order_by("-id").first()
        print(order)
        order_log(order)
        
