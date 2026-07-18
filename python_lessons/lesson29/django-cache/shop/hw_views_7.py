import time
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache
from .models import MyModel # Zastąp swoim modelem

@api_view(['GET'])
def selective_cache_view(request):
    fast_db_data = MyModel.objects.values_list('name', flat=True)[:5]
    
    cache_key = 'complex_calculation_result'
    complex_result = cache.get(cache_key)
    
    if complex_result is None:
        time.sleep(3)
        complex_result = {
            "status": "obliczono pomyślnie",
            "value": 42
        }
        cache.set(cache_key, complex_result, 3600)
        
    return Response({
        "recent_models": list(fast_db_data),
        "computation": complex_result
    })