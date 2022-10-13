from django.db import models
from django.contrib.auth import get_user_model

from apps.posts.models import Post

User = get_user_model()


class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='like'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='like'
    )
    create_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ("-create_at",)

    def __str__(self):
        return f"{self.post.id} --- {self.user.username_telegram}"
