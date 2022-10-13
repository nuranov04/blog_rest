from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.users.managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = None
    telegram_id = models.CharField(
        max_length=256,
        unique=True
    )
    first_name = models.CharField(
        max_length=256,
        blank=True, null=True
    )
    last_name = models.CharField(
        max_length=256,
        blank=True, null=True
    )
    username_telegram = models.CharField(
        max_length=256,
        unique=True
    )
    id_telegram = models.CharField(
        max_length=16
    )
    create_at = models.DateTimeField(
        auto_now_add=True
    )

    USERNAME_FIELD = "username_telegram"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ("-create_at",)

    def __str__(self):
        return f"{self.username_telegram}"
