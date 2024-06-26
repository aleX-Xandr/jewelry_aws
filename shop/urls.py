from django.urls import path

from shop import views

urlpatterns = [
    path('category/', views.categories, name='categories'),
    path('category/<slug>/', views.category, name='category'),
    path('product/<slug>/', views.product, name='product'),

    path('constructor/', views.constructor, name='constructor'),
]
