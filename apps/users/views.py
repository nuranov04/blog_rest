from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from apps.users.serializers import UserSerializer, UserDetailSerializer
from apps.users.models import User


class UserApiViewSet(GenericViewSet,
                     ListModelMixin,
                     RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        print(self.action)
        if self.action in ("retrieve", "update", "partial_update",):
            return UserDetailSerializer
        return UserSerializer
