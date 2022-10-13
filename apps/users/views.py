from rest_framework import viewsets
from rest_framework.decorators import action

from apps.users.serializers import UserSerializer
from apps.users.models import User


class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
