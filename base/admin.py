from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.shortcuts import redirect

from base.models import ContactRequest, Contact, Page, AboutImage, Setting, Social


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def changelist_view(self, request, extra_context=None):
        settings = Setting.get_settings()
        return redirect(request.path + f'{settings.id}/')


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'sort']
    list_editable = ['sort']


class PageAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(), label="Text")

    class Meta:
        model = Page
        fields = '__all__'


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm

    list_display = ['name', 'slug']


@admin.register(AboutImage)
class AboutImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'sort']
    list_editable = ['sort']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone']


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'created_at']
