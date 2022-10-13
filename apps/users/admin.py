from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'telegram_id',
        'username_telegram',
        'create_at'
    )
    search_fields = (
        'telegram_id',
        'username_telegram',
        'create_at',
    )
