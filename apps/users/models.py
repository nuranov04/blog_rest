from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = None
    id_telegram = models.CharField(
        primary_key=True,
        max_length=100,
        unique=True,
        verbose_name=_("ID Telegram")
    )
    username_telegram = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("Username Telegram")
    )

    USERNAME_FIELD = "username_telegram"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ("-id_telegram",)

    def __str__(self):
        return self.username_telegram

