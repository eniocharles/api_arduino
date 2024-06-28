from django.urls import path
from .views import WaterHumidityListCreate, WaterHumidityDetail

urlpatterns = [
    path('humidity/', WaterHumidityListCreate.as_view(), name='humidity-list-create'),
    path('humidity/<int:pk>/', WaterHumidityDetail.as_view(), name='humidity-detail'),
]