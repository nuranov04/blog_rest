from rest_framework import serializers
from rest_framework.response import Response

from apps.likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data["user"].id_telegram)
        print(validated_data["post"].id)
        if Like.objects.filter(user=validated_data["user"].id_telegram, post=validated_data["post"].id).count() < 1:
            return Like.objects.create(**validated_data)
        raise serializers.ValidationError({"error": "you cannot like again"})
