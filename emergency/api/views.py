from rest_framework import generics

from emergency import models
from . import serializers

class AmbulanceListView(generics.ListAPIView):
    queryset = models.Ambulance.objects.all()
    serializer_class = serializers.AmbulanceSerializer