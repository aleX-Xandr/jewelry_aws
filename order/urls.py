from django.urls import path

from order import views

urlpatterns = [
    path('order/', views.order, name='order'),
    path('order/edit/', views.edit, name='order_edit'),
    path('order/delete/', views.delete, name='order_delete'),
]
