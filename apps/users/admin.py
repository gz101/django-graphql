from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User 


class CustomUser(UserAdmin):
    model = User 
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('address',)}),
    )


admin.site.register(User, CustomUser)
