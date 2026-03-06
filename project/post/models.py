from django.db import models

# Create your models here.

class Farm(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    size_hectares = models.FloatField()
    crop_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SensorNode(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='sensor_nodes')
    node_code = models.CharField(max_length=50, unique=True)
    installed_at = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('active', 'Active'),
        ('offline', 'Offline'),
        ('maintenance', 'Maintenance'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='active')

    def __str__(self):
        return f"{self.node_code} ({self.farm.name})"

class SensorData(models.Model):
    sensor_node = models.ForeignKey(SensorNode, on_delete=models.CASCADE, related_name='data')
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()
    soil_ph = models.FloatField()
    light_intensity = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sensor_node.node_code} @ {self.timestamp}"

class DiseasePrediction(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='disease_predictions')
    predicted_disease = models.CharField(max_length=100)
    risk_level_choices = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    risk_level = models.CharField(max_length=10, choices=risk_level_choices)
    confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class IrrigationRecommendation(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='irrigation_recommendations')
    recommendation = models.CharField(max_length=100)
    water_amount_liters = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class YieldForecast(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='yield_forecasts')
    predicted_yield = models.FloatField()
    confidence = models.FloatField()
    forecast_date = models.DateField()