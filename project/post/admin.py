from django.contrib import admin
from .models import Farm, SensorNode, SensorData, DiseasePrediction, IrrigationRecommendation, YieldForecast

# Register your models here.

admin.site.register(Farm)
admin.site.register(SensorNode)
admin.site.register(SensorData)
admin.site.register(DiseasePrediction)
admin.site.register(IrrigationRecommendation)
admin.site.register(YieldForecast)

