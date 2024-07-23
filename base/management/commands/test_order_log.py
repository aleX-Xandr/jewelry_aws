import requests
from django.core.management import BaseCommand

from jewelry import settings
from order.models import Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        order = Order.objects.filter().first()
        print(order)

        positions_text = ""
        for product in order.products.all():
            text = f"Название: {product.product.name}\n" \
                   f"Стоимость: {product.get_price()} ({product.quantity} шт.)\n\n"
            positions_text += text

        text = f"Новый заказ #{str(order.id).split('-')[0]}\n\n" \
               f"Стоимость: {order.get_price()}\n\n" \
               f"Товары:\n\n{positions_text}" \

        print(text)

        url = settings.TELEGRAM_LOG_URL
        data = {
            "chat_id": settings.TELEGRAM_CHAT_ID,
            "text": text,
        }
        response = requests.post(url, json=data).text
        print(response)
