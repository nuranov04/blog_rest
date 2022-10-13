from rest_framework.routers import DefaultRouter

from apps.likes.views import LikeApiViewSet

router = DefaultRouter()
router.register(
    prefix='',
    viewset=LikeApiViewSet
)

urlpatterns = router.urls
