from rest_framework import serializers

from emergency import models

class AmbulanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ambulance
        fields = ('pk', 'traffic_code',)
    

    """
    {
        'pk': 1,
        'traffic_code': "34 ABC 123"
    }
    """