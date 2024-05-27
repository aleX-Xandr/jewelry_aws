from django.urls import path

from base import views

urlpatterns = [
    path('about-us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('contact/request/', views.contact_request, name='contact_request'),
]
