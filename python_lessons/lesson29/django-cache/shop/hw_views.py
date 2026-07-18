from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.cache import cache_page

@api_view(['GET'])
@cache_page(60)
def get_item_list(request):
    data = {
        "items": ["Jabłko", "Banan", "Pomarańcza"],
        "message": "To jest lista owoców."
    }
    return Response(data)