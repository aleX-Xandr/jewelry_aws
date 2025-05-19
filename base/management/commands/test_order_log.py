import requests
from django.core.management import BaseCommand

from jewelry import settings
from order.models import Order
from order.hooks import order_log


class Command(BaseCommand):
    def handle(self, *args, **options):
        order = Order.objects.filter().all()[-1]
        print(order)
        order_log(order)
        
