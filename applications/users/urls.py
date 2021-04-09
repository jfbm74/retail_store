from rest_framework import routers

from .viewsets import UserViewSet

router = routers.SimpleRouter()
router.register('api/v1.0/users', UserViewSet)

urlpatterns = router.urls
