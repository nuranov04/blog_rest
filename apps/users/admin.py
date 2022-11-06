from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id_telegram',
        'username_telegram',
    )
    search_fields = (
        'id_telegram',
        'username_telegram',
    )
