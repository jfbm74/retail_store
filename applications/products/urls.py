from rest_framework import routers

from .viewsets import ProductViewSet

router = routers.SimpleRouter()
router.register('api/v1.0/products', ProductViewSet)

urlpatterns = router.urls
