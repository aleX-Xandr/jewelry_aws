from django.contrib import admin
from django.contrib.auth.models import Group

from user.models import User

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    fields = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser', 'password']
    exclude = ['last_login', 'groups', 'user_permissions', 'date_joined']
