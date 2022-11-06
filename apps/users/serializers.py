from rest_framework import serializers

from apps.users.models import User
from apps.posts.serializers import PostSerializer


class UserSerializer(serializers.ModelSerializer):
    post = PostSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = (
            'id_telegram',
            'first_name',
            'last_name',
            'username_telegram',
            'password',
            'post'
        )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
