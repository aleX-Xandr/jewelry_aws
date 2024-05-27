from django.contrib import admin

from shop.models import Material, Product, ProductImage, Category


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']


class ProductImageInlineAdmin(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'quantity']
    list_editable = ['quantity']

    inlines = [ProductImageInlineAdmin]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
