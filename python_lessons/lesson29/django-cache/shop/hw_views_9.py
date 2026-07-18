from rest_framework import viewsets
from rest_framework.response import Response
from django.core.cache import cache
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        cache_key = f"mymodel_detail_{instance.id}"
        
        cached_data = cache.get(cache_key)
        if not cached_data:
            cached_data = super().retrieve(request, *args, **kwargs)
            cache.set(cache_key, cached_data.data, 60 * 10) # Cache na 10 minut
        return Response(cached_data)
    
    def perform_update(self, serializer):
        instance = serializer.save()
        cache_key = f'mymodel_detail_{instance.id}'
        cache.delete(cache_key)