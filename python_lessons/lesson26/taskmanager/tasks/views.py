from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('-created_at') # Jakie dane mają być dostępne
    serializer_class = TaskSerializer # Jakiego serializatora użyć do "tłumaczenia"
    
    # create
    # destroy
    # update
    # def update(self, request, *args, **kwargs):
    #     ...
    #     super().update(self, request, *args, **kwargs)