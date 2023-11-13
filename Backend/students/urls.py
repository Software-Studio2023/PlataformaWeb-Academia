from rest_framework import routers
from django.urls import path, include
from .api import studentsViewSet
from .views import SignIn
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()

router.register('api/students', studentsViewSet, 'students')


urlpatterns = [
  path('', include(router.urls)),
  path('api/auth/login/', SignIn.as_view(), name='auth_login'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]