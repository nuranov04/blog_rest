from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


schema_view = get_schema_view(
    openapi.Info(
        title="Aiogram Bot API",
        default_version='',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="artnyr2004@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

api_urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('posts/', include('apps.posts.urls')),
    path('likes/', include('apps.likes.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(api_urlpatterns)),
    path('', include('rest_framework.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
