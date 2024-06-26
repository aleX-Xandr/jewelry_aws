from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from base.models import Page
from shop.models import Category, Product


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

    context = {
        "product": product,
        "recommend_products": recommend_products,
    }
    return render(request, 'product.html', context=context)


def constructor(request):
    pass
