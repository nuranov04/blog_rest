from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username_telegram, password, **extra_fields):
        if not username_telegram:
            raise ValueError('The Username Telegram must be set')
        user = self.model(username_telegram=username_telegram, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username_telegram, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        if extra_fields.get("is_superuser") is False:
            raise ValueError("Super users must have is_superuser=True")
        return self.create_user(username_telegram, password, **extra_fields)
