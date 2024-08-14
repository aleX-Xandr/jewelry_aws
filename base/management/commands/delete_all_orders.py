from django.core.management import BaseCommand

from order.models import Order


class Command(BaseCommand):
    Order.objects.all().delete()
