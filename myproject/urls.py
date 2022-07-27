from django.contrib import admin
from django.urls import path, include, re_path
import jwt
from rest_framework_simplejwt import views as jwt_views
# Swagger Configurations
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="BLOGAPP BACKEND",
        default_version='v1',
        description="BLOG APP BACKEND BY SAGNIK BANIK",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('myapi.urls')),

    path(
        'api/swagger/',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0
        ),
        name='schema-swagger-ui'
    ),
     
    path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns+=static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)