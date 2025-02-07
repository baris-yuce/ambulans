from rest_framework import viewsets

from .. import models
from . import serializers


class AmbulanceViewSet(viewsets.ModelViewSet):
    model = models.Ambulance
    serializer_class = serializers.AmbulanceSerializer
    queryset = model.objects.all()


class StationInfoViewSet(viewsets.ModelViewSet):
    model = models.StationInfo
    serializer_class = serializers.StationInfoSerializer
    queryset = model.objects.all()


class StandardEquipmentViewSet(viewsets.ModelViewSet):
    model = models.StandardEquipment
    serializer_class = serializers.StandardEquipmentSerializer
    queryset = model.objects.all()

