from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'id_telegram',
            'first_name',
            'last_name',
            'username_telegram',
            'create_at'
        )
