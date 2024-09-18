from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from base.models import Page
from base.service import back
from order.models import OrderProduct
from order.service import order_service
from shop.models import Product, Bracelet

from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.urls import reverse


def order(request):
    page = get_object_or_404(Page, slug='order')

    host = request.get_host()
    order = order_service.get_order(request)

    if request.method == 'POST':
        order.address = request.POST.get('address', '')
        order.contact = request.POST.get('contact', '')
        order.delivery = bool(request.POST.get('delivery', ''))
        order.save()
        return redirect('order')

    if order.address and order.contact:
        paypal_checkout = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": order.get_price(),
            "item_name": f"ORDER #{order.id}",
            "invoice": f"{order.id}",
            "currency_code": "EUR",
            "notify_url": f"https://{host}{reverse('paypal-ipn')}",
            "return_url": f"https://{host}{reverse('index')}",
            "cancel_url": f"https://{host}{reverse('index')}",
        }
        paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)
    else:
        paypal_payment = None

    context = {
        "page": page,
        "paypal": paypal_payment,
    }
    return render(request, 'order.html', context=context)


def edit(request):
    order = order_service.get_order(request)

    product_id = request.GET.get('product_id')
    quantity = int(request.GET.get('quantity'))
    ajax = request.GET.get('ajax')

    product = Product.objects.filter(id=product_id)
    if not product:
        return JsonResponse({"status": False, "message": "product_not_found"})
    else:
        product = product.first()

    if quantity > product.quantity:
        quantity = product.quantity
        return JsonResponse({"status": False, "message": "invalid_quantity"})

    check_product = order.products.filter(product=product)
    if not check_product:
        if quantity <= 0:
            return redirect(back(request))

        check_product = OrderProduct(
            order=order,
            product=product,
            quantity=quantity)
        check_product.save()
    else:
        check_product = check_product.first()

        if quantity == 0:
            check_product.delete()
        else:
            check_product.quantity = quantity
            check_product.save()
    if ajax:
        return JsonResponse({"status": True, "order_price": order.get_price(), 'product_price': check_product.get_price()})
    else:
        return redirect('order')


def delete(request):
    order = order_service.get_order(request)

    product_id = request.GET.get('product_id')
    bracelet_id = request.GET.get('bracelet_id')
    if product_id:
        product = Product.objects.filter(id=product_id)
        if not product:
            return JsonResponse({"status": False, "message": "product_not_found"})
        else:
            product = product.first()

        order.products.filter(product=product).delete()
    elif bracelet_id:
        bracelet = Bracelet.objects.filter(id=bracelet_id)
        if not bracelet:
            return JsonResponse({"status": False, "message": "bracelet_not_found"})
        else:
            bracelet = bracelet.first()

        order.bracelets.filter(bracelet=bracelet).delete()
    return redirect('order')
