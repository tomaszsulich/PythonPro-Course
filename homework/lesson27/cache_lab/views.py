import time

from django.contrib.auth.models import User
from django.core.cache import cache
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


def cache_test(request):
    return render(
        request,
        "cache_lab/cache_test.html",
    )


@cache_page(60)
@api_view(["GET"])
def product_list(request):
    return Response(
        {
            "products": [
                {"id": 1, "name": "Kanapka z jajkiem"},
                {"id": 2, "name": "Tost z szynką i serem"},
            ]
        }
    )


@api_view(["GET"])
def selective_cache_view(request):
    user_count = User.objects.count()

    cache_key = "complex_calculation_result"
    complex_result = cache.get(cache_key)

    if complex_result is None:
        time.sleep(3)
        complex_result = 42
        cache.set(cache_key, complex_result, timeout=60)
        source = "calculated"
    else:
        source = "cache"

    return Response(
        {
            "user_count": user_count,
            "complex_result": complex_result,
            "source": source,
        }
    )


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @method_decorator(cache_page(60 * 10))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        cache_key = f"product_detail_{product_id}"

        cached_product = cache.get(cache_key)

        if cached_product is not None:
            return Response(cached_product)

        product = self.get_object()
        serializer = self.get_serializer(product)

        cache.set(
            cache_key,
            serializer.data,
            timeout=60,
        )

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

        product_id = serializer.instance.pk
        cache_key = f"product_detail_{product_id}"

        cache.delete(cache_key)