from django.shortcuts import render
from rest_framework import generics
from .models import WaterHumidity
from .serializers import WaterHumiditySerializer

class WaterHumidityListCreate(generics.ListCreateAPIView):
    queryset = WaterHumidity.objects.all() #Define o conjunto de dados que será manipulado pela visualização. Aqui, estamos obtendo todas as instâncias de WaterHumidity
    serializer_class = WaterHumiditySerializer #Especifica qual serializador deve ser usado para esta visualização, que é o WaterHumiditySerializer.

class WaterHumidityDetail(generics.RetrieveUpdateDestroyAPIView): #Esta visão aborda operações disciplinares ( GET, PUT, PATCH, DELETE) em instâncias individuais de WaterHumidity
    queryset = WaterHumidity.objects.all() #msm coisa q a ulitma
    serializer_class = WaterHumiditySerializer #msm coisa q a ultima tbm
    
'''
Operações Suportadas:
GET : Retorna uma lista de todas as instâncias de WaterHumidity.
POST : Cria uma nova instância de WaterHumiditycom os dados fornecidos na requisição.'''