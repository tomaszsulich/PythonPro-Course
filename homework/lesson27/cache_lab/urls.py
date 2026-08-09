from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    ProductViewSet,
    cache_test,
    product_list,
    selective_cache_view,
)


router = DefaultRouter()
router.register("viewset-products", ProductViewSet)


urlpatterns = [
    path("cache-test/", cache_test, name="cache-test"),
    path("products/", product_list, name="product-list"),
    path("selective-cache/", selective_cache_view, name="selective-cache"),
]

urlpatterns += router.urls