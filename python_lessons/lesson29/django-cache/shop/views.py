from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Address, Client, Category, Product, Transaction
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema
from .serializers import (AddressSerializer, ClientSerializer,
                          CategorySerializer, ProductSerializer,
                          TransactionReadSerializer,
                          TransactionWriteSerializer)


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    
    @extend_schema(tags=['list', 'adresses'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().select_related('address')
    serializer_class = ClientSerializer
    

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().prefetch_related('product')
    serializer_class = CategorySerializer
    
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category')
    serializer_class = ProductSerializer
    
    
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().select_related(
        'client').prefetch_related('items__product')
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TransactionWriteSerializer
        return TransactionReadSerializer
    
    @action(detail=False, methods=['get'])
    def current_user(self, request):
        return Response({"username": request.user.username})