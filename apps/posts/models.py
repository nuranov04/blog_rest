from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='post'
    )
    title = models.CharField(
        max_length=256,
    )
    description = models.TextField()
    image = models.URLField()
    create_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ("-create_at",)

    def __str__(self):
        return f"{self.user.username_telegram} -- {self.title} --- {self.create_at}"

