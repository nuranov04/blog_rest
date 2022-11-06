from django.db import models
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response

from apps.posts.models import Post


User = get_user_model()


class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='like',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    create_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ("-create_at",)

    def __str__(self):
        return f"{self.post.id} --- {self.user.username_telegram}"

    def save(self, *args, **kwargs):
        if Like.objects.filter(user=self.user.id_telegram, post=self.post.id).count() < 1:
            return super().save(*args, **kwargs)