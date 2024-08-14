from django.core.management import BaseCommand

from order.models import Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        Order.objects.all().delete()
