from django.contrib import admin

from order.models import Order, OrderProduct


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'address', 'contact', 'get_price', 'status']
    search_fields = ['id']
    list_filter = ['status']

    inlines = [OrderProductInline]
