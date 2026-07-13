from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task  # Wskazujemy, który model ma być serializowany
        fields = '__all__'
        
    # def validate(self, data: dict):
    #     ...
    
    # def validate_title(self, value):
    #     if not isinstance(value, str) or len(value) < 3:
    #         raise ValueError()