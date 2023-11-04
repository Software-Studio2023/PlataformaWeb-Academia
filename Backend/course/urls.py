from rest_framework import routers
from .api import CourseViewSet

router = routers.DefaultRouter()

router.register('api/curso', CourseViewSet, 'course')

urlpatterns = router.urls