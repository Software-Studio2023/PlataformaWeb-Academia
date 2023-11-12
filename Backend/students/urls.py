from rest_framework import routers
from django.urls import path, include
from .api import studentsViewSet
from .views import Login

router = routers.DefaultRouter()

router.register('api/students', studentsViewSet, 'students')


urlpatterns = [
  path('', include(router.urls)),
  path('api/auth/login/', Login.as_view(), name='auth_login')
]