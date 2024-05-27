from django.contrib import admin

from base.models import ContactRequest, Contact, Page, AboutImage


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(AboutImage)
class AboutImageAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone']


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
