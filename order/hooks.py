import requests
from django.conf import settings
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received

from order.models import Order


def webhook_handler(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        if ipn_obj.receiver_email != settings.PAYPAL_RECEIVER_EMAIL:
            error_order_log('invalid_receiver')
            return

        order_id = ipn_obj.invoice
        order = Order.objects.filter(id=order_id).first()
        order.status = 'success'
        order.save()
        order_log(order)
    else:
        error_order_log('unsuccessful_payment')
        return


valid_ipn_received.connect(webhook_handler)


def send_log(text):
    url = settings.TELEGRAM_LOG_URL
    data = {
        "chat_id": settings.TELEGRAM_CHAT_ID,
        "text": text,
    }
    response = requests.post(url, json=data).text
    print(response)


def error_order_log(reason):
    if reason == 'invalid_receiver':
        send_log('ERROR PAYPAL: INVALID RECEIVER')
    elif reason == 'unsuccessful_payment':
        send_log('ERROR PAYPAL: UNSUCCESSFUL PAYMENT')


def order_log(order: Order):
    positions_text = ""
    for product in order.products.all():
        text = f"Название: {product.product.name}\n" \
               f"Стоимость: {product.get_price()} ({product.quantity} шт.)\n\n"
        positions_text += text

    text = f"Новый заказ #{str(order.id).split('-')[0]}\n\n" \
           f"Стоимость: {order.get_price()}\n" \
           f"Адрес: {order.address}\n" \
           f"Контакты: {order.contact}\n\n" \
           f"Товары:\n\n{positions_text}"
    print(text)
    send_log(text)
