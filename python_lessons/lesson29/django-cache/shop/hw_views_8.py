from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    
    @method_decorator(cache_page(60 * 10))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    
    # http://127.0.0.1:8000/api/mymodels/1/
    @method_decorator(cache_page(60 * 1))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)