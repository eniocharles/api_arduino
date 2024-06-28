from rest_framework import serializers 
from .models import WaterHumidity 

class WaterHumiditySerializer(serializers.Serializer):
    class Meta:
        model = WaterHumidity
        fields = ['id', 'humidity', 'timestamp']