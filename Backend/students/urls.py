from rest_framework import routers
from .api import studentsViewSet

router = routers.DefaultRouter()

router.register('api/students', studentsViewSet, 'students')

urlpatterns = router.urls