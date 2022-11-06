from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, DestroyModelMixin

from .models import Post
from .serializers import PostSerializer, PostDetailSerializer


class PostApiViewSet(GenericViewSet,
                     ListModelMixin,
                     RetrieveModelMixin,
                     DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    search_fields = [
        "title", "description",
        "create_at", "user",
    ]

    def get_serializer_class(self):
        if self.action in ("retrieve", "update",):
            return PostDetailSerializer
        return self.serializer_class
