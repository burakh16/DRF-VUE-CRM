from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from customers.api.views import CustomerViewSet
from products.api.views import ProductViewSet
from orders.api.views import OrderViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("customer", CustomerViewSet)
router.register("product", ProductViewSet)
router.register("order", OrderViewSet)


urlpatterns = router.urls