from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from base.models import Page
from order.service import order_service
from shop.models import Category, Product, Bracelet, Material


def categories(request):
    categories = Category.objects.filter()
    page = get_object_or_404(Page, slug='categories')
    context = {
        "categories": categories,
        "page": page,
    }
    return render(request, "categories.html", context=context)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()

    p = Paginator(products, 12)
    page_num = request.GET.get('page', 1)
    page = p.page(page_num)

    context = {
        "category": category,
        "page": page,
    }
    return render(request, 'products.html', context=context)


def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    recommend_products = Product.objects.filter().order_by('?')[:4]

    materials = Material.objects.filter()
    material_get = request.GET.get('material')
    if not material_get:
        material = materials.first()
    else:
        material = Material.objects.filter(id=material_get).first()

    images = product.images.filter(material=material)

    context = {
        "product": product,
        "recommend_products": recommend_products,
        "images": images,

        "materials": materials,
        "chosen_material": material,
    }
    return render(request, 'product.html', context=context)


def constructor(request):
    category_constructor = Category.objects.filter(is_coulomb=True)[0]
    page = get_object_or_404(Page, slug='constructor')

    order = order_service.get_order(request)
    products = []
    for prod in order.products.filter(product__category=category_constructor):
        for i in range(prod.quantity):
            new_prod = prod.product
            new_prod.id = str(new_prod.id) + str(i)
            products.append(new_prod)

    context = {
        "products": products,
        "page": page,
    }
    return render(request, 'constructor.html', context=context)


# def constructor_save(request):
#     selected_items = request.POST.get('selected_items').split(',')
#
#     bracelet = Bracelet()
#     bracelet.save()
#     for item in selected_items:
#         product = Product.objects.get(id=item)
#         bracelet.products.add(product)
#
#     order = order_service.get_order(request)
#     brac = OrderBracelet(
#         order=order,
#         bracelet=bracelet)
#     brac.save()
#     return redirect('order')
