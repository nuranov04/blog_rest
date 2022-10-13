from django.contrib import admin

from .models import Post


@admin.register(Post)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )
    list_filter = (
        'user',
        'title',
        'create_at',
    )
