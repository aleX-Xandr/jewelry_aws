from django.shortcuts import render, redirect, get_object_or_404

from base.models import ContactRequest, Contact, Page, AboutImage
from shop.models import Product


def index(request):
    slide_products = Product.objects.filter().order_by('?')[:4]
    collections = Product.objects.filter().order_by('?')[:6]
    coming_soon = Product.objects.filter().order_by('?')[:4]
    you_may_also_like = Product.objects.filter().order_by('?')[:6]

    page = get_object_or_404(Page, slug='index')
    context = {
        "slide_products": slide_products,
        "collections": collections,
        "coming_soon": coming_soon,
        "you_like": you_may_also_like,
        "page": page,
    }
    return render(request, 'index.html', context=context)


def about_us(request):
    images = AboutImage.objects.filter()

    first_block = images[:3]
    second_block = images[3:]

    page = get_object_or_404(Page, slug='about')
    context = {
        "page": page,
        "first_block": first_block,
        "second_block": second_block,
    }
    return render(request, 'about.html', context=context)


def contact(request):
    contacts = Contact.objects.filter()
    page = get_object_or_404(Page, slug='contact')
    context = {
        "contacts": contacts,
        "page": page,
    }
    return render(request, 'contacts.html', context=context)


def contact_request(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    contact_req = ContactRequest(
        name=name,
        email=email,
        message=message)
    contact_req.save()
    return redirect('contact')
