from rest_framework import routers

from .viewsets import OrderViewSet

router = routers.SimpleRouter()
router.register('api/v1.0/orders', OrderViewSet)

urlpatterns = router.urls
