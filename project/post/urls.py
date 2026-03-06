from django.urls import path
from .views import (
    FarmListCreateAPIView, FarmRetrieveUpdateDestroyAPIView,
    SensorNodeListCreateAPIView, SensorNodeRetrieveUpdateDestroyAPIView,
    SensorDataListAPIView, DiseasePredictionListAPIView,
    IrrigationRecommendationListAPIView, YieldForecastListAPIView
)

# post/urls.py logic check
urlpatterns = [
    # Ensure these names match what your frontend might look for
    path('farms/', FarmListCreateAPIView.as_view(), name='farm-list-create'),
    path('farms/<int:pk>/', FarmRetrieveUpdateDestroyAPIView.as_view(), name='farm-rud'), # Required for Delete/Update
    
    path('sensornodes/', SensorNodeListCreateAPIView.as_view(), name='sensornode-list-create'),
    path('sensornodes/<int:pk>/', SensorNodeRetrieveUpdateDestroyAPIView.as_view(), name='sensornode-rud'), # Required for Delete/Update

    # Dashboard endpoints used by getSensorData(), getDisease(), etc.
    path('sensordata/', SensorDataListAPIView.as_view(), name='sensordata-list'),
    path('diseasepredictions/', DiseasePredictionListAPIView.as_view(), name='disease-list'),
    path('irrigation/', IrrigationRecommendationListAPIView.as_view(), name='irrigation-list'),
    path('yieldforecast/', YieldForecastListAPIView.as_view(), name='yield-list'),
]