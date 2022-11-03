from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from measurement.models import Sensor, Measurement

class MeasurementSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = "__all__"

class SensorSerialiazer(serializers.ModelSerializer):
    measurements = MeasurementSerialiazer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'desc', 'measurements']
