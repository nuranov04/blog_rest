from rest_framework import serializers

from .models import Post
from apps.likes.serializers import LikeSerializer


class PostDetailSerializer(serializers.ModelSerializer):
    like = LikeSerializer(many=True, read_only=True)
    total_likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "user",
            "total_likes",
            "title",
            "description",
            "image",
            "create_at",
            "like"
        )

    def get_total_likes(self, instance):
        print(instance.like.all().count())
        return instance.like.all().count()


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "user",
            "title",
            "description",
            "image",
            "create_at",
        )
