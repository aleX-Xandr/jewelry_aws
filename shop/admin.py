from django.contrib import admin
from django.template.defaultfilters import slugify

from shop.models import Material, Product, ProductImage, Category


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']


class ProductImageInlineAdmin(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'quantity', 'slug', 'sort']
    list_editable = ['quantity', 'sort']
    exclude = ['slug']

    inlines = [ProductImageInlineAdmin]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.slug = slugify(obj.name) + "-" + str(obj.id).split('-')[0]
        super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'sort', 'is_coulomb']
    list_editable = ['sort', 'is_coulomb']
    exclude = ['slug']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.slug = slugify(obj.name) + "-" + str(obj.id).split('-')[0]
        super().save_model(request, obj, form, change)
