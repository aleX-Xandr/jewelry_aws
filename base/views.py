from django.shortcuts import render, redirect, get_object_or_404

from base.models import ContactRequest, Contact, Page, AboutImage


def about_us(request):
    images = AboutImage.objects.filter()
    page = get_object_or_404(Page, slug='about')
    context = {
        "page": page,
        "images": images,
    }
    pass


def contact(request):
    contacts = Contact.objects.filter()
    page = get_object_or_404(Page, slug='contact')
    context = {
        "contacts": contacts,
        "page": page,
    }
    pass


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
