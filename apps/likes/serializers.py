from rest_framework import serializers

from apps.likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

    def create(self, validated_data):
        if Like.objects.filter(user=validated_data["user"].id_telegram, post=validated_data["post"].id).count() < 1:
            return Like.objects.create(**validated_data)
        raise serializers.ValidationError({"error": "you cannot like again"})
