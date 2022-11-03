# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView
from measurement.models import Sensor
from rest_framework.response import Response
from .serializers import SensorSerialiazer, MeasurementSerialiazer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialiazer

    def perform_create(self, serializer):
        return serializer.save(name=self.request.data.get('name'), desc=self.request.data.get('desc'))

class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialiazer

    def patch(self, request, *args, **kwargs):
        sensor = self.get_queryset().first()
        print(request.data)
        serializer = SensorSerialiazer(sensor, data=request.data, partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=200)
        return Response(data="Unexpected Parameters", status=400)

class MeasurementsView(CreateAPIView):
    serializer_class = MeasurementSerialiazer
