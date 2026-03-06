from django.core.management.base import BaseCommand
from post.models import *
import random
import time


class Command(BaseCommand):

    help = "Generate simulated sensor data"

    def handle(self, *args, **kwargs):

        if Farm.objects.count() == 0:

            farm = Farm.objects.create(
                name="Demo Farm",
                location="Philippines",
                size_hectares=5,
                crop_type="Rice"
            )

            node = SensorNode.objects.create(
                farm=farm,
                node_code="NODE-001"
            )

        node = SensorNode.objects.first()

        while True:

            temp = random.uniform(25, 35)
            humidity = random.uniform(50, 80)
            moisture = random.uniform(20, 60)
            ph = random.uniform(5.5, 7.5)
            light = random.uniform(200, 900)

            SensorData.objects.create(
                sensor_node=node,
                temperature=temp,
                humidity=humidity,
                soil_moisture=moisture,
                soil_ph=ph,
                light_intensity=light
            )

            print("Sensor data inserted")

            time.sleep(5)