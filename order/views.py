from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from base.models import Page
from order.models import OrderProduct
from order.service import order_service
from shop.models import Product


def order(request):
    page = get_object_or_404(Page, slug='order')
    context = {
        "page": page,
    }
    return render(request, 'order.html', context=context)


def edit(request):
    order = order_service.get_order(request)

    product_id = request.GET.get('product_id')
    quantity = request.GET.get('quantity')
    if quantity < 0:
        return JsonResponse({"status": False, "message": "invalid_quantity"})

    product = Product.objects.filter(id=product_id)
    if not product:
        return JsonResponse({"status": False, "message": "product_not_found"})
    else:
        product = product.first()

    if quantity > product.quantity:
        return JsonResponse({"status": False, "message": "invalid_quantity"})

    check_product = order.products.filter(product=product)
    if not check_product:
        check_product = OrderProduct(
            order=order,
            product=product,
            quantity=quantity)
    else:
        check_product = check_product.first()

        if quantity == 0:
            check_product.delete()
        else:
            check_product.quantity = quantity
    check_product.save()
    return redirect('order')


def delete(request):
    order = order_service.get_order(request)

    product_id = request.GET.get('product_id')
    product = Product.objects.filter(id=product_id)
    if not product:
        return JsonResponse({"status": False, "message": "product_not_found"})
    else:
        product = product.first()

    order.products.filter(product=product).delete()
    return redirect('order')
