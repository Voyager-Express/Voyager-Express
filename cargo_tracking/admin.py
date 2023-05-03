from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active',)
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('address', 'phone', 'role')})
    )

    add_fieldsets = (
        (None, {
        'classes': ("wide",),
        'fields': ('email', 'user_name', 'first_name', 'last_name', 'password1', 'password2', 'address', 'phone', 'role',)}
        ),
    )



admin.site.register(User, UserAdminConfig)
