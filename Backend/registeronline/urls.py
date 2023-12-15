from rest_framework import routers
from .api import RegisterViewSet

router = routers.DefaultRouter()

router.register('api/registeronline', RegisterViewSet, 'register')

urlpatterns = router.urls