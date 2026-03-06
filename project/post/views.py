from rest_framework import generics
from .models import Farm, SensorNode, SensorData, DiseasePrediction, IrrigationRecommendation, YieldForecast
from .serializers import (
    FarmSerializer, SensorNodeSerializer, SensorDataSerializer,
    DiseasePredictionSerializer, IrrigationRecommendationSerializer, YieldForecastSerializer
)

# Admin CRUD
class FarmListCreateAPIView(generics.ListCreateAPIView):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

class FarmRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

class SensorNodeListCreateAPIView(generics.ListCreateAPIView):
    queryset = SensorNode.objects.all()
    serializer_class = SensorNodeSerializer

class SensorNodeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SensorNode.objects.all()
    serializer_class = SensorNodeSerializer

# Read-only (for Dashboard)
class SensorDataListAPIView(generics.ListAPIView):
    queryset = SensorData.objects.all().order_by('-timestamp')
    serializer_class = SensorDataSerializer

class DiseasePredictionListAPIView(generics.ListAPIView):
    queryset = DiseasePrediction.objects.all().order_by('-created_at')
    serializer_class = DiseasePredictionSerializer

class IrrigationRecommendationListAPIView(generics.ListAPIView):
    queryset = IrrigationRecommendation.objects.all().order_by('-created_at')
    serializer_class = IrrigationRecommendationSerializer

class YieldForecastListAPIView(generics.ListAPIView):
    queryset = YieldForecast.objects.all().order_by('-forecast_date')
    serializer_class = YieldForecastSerializer