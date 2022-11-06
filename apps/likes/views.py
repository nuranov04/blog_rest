from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import DestroyModelMixin, CreateModelMixin

from apps.likes.serializers import LikeSerializer
from apps.likes.models import Like


class LikeApiViewSet(GenericViewSet,
                     DestroyModelMixin,
                     CreateModelMixin):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
