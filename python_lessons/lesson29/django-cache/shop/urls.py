from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddressViewSet, ClientViewSet, CategoryViewSet, ProductViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'addresses', AddressViewSet),
router.register(r'clients', ClientViewSet)
router.register(r'categories', CategoryViewSet),
router.register(r'products', ProductViewSet),
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('',
         include(router.urls)), # Poprawione: usunięto powtarzające się 'api/'
]