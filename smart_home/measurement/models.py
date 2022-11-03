from decimal import Decimal

from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    desc = models.CharField(max_length=100, blank=True, null=True, verbose_name='Описание датчика')


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=20, decimal_places=1, default=Decimal(0.0), verbose_name='Температура при измерении')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')
    image = models.ImageField(blank=True)