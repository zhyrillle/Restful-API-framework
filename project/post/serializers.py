from rest_framework import serializers
from .models import Farm, SensorNode, SensorData, DiseasePrediction, IrrigationRecommendation, YieldForecast

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'

class SensorNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorNode
        fields = '__all__'

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'

class DiseasePredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseasePrediction
        fields = '__all__'

class IrrigationRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IrrigationRecommendation
        fields = '__all__'

class YieldForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = YieldForecast
        fields = '__all__'