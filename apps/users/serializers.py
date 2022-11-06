from rest_framework import serializers

from apps.users.models import User
from apps.posts.serializers import PostDetailSerializer
from apps.likes.serializers import LikeSerializer


class UserDetailSerializer(serializers.ModelSerializer):
    post = PostDetailSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    total_likes = serializers.SerializerMethodField(read_only=True)
    total_posts = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id_telegram',
            'first_name',
            'last_name',
            'username_telegram',
            'total_likes',
            'total_posts',
            'post',
            'likes',
        )

    def get_total_likes(self, instance):
        return instance.likes.all().count()

    def get_total_posts(self, instance):
        return instance.post.all().count()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id_telegram',
            'first_name',
            'last_name',
            'username_telegram',
            'password',
        )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
