from rest_framework import viewsets

from apps.likes.serializers import LikeSerializer
from apps.likes.models import Like


class LikeApiViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
