from rest_framework import serializers

from emergency import models

class AmbulanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ambulance
        fields = ['pk', 'plate', 'ambulance_type', 'stations']
        read_only_fields = ['created_at', 'updated_at'] # response -> OK
                                                       # request -> X NO
        depth = 1
        # Kendisi ile ilişkili bir tablo varsa onun da içeriğini gösterip göstermeyceğine karar verir
        # bu sınıf için stations ile istasyon bilgilerinin gönderilip gönderilmeyeceğini belirtir.
        # kaç ile sınırlandıysa o kadar ilişki arar.
        

class StationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StationInfo
        fields = ['pk', 'station_name', 'station_code', 'ambulances']
        depth = 1


class StandardEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StandardEquipment
        fields = '__all__'
    

    """
    a = {
        'pk': 1,
        'traffic_code': "34 ABC 123"
    } -> python dictionary data type
    integer -> 1 2 3 25
    float -> 1.5 8.2382938
    string -> "Merhaba Zalim Dünya"
    list (array) -> [1, 2, "a"]
    dictionary (Map) -> JSON
    dict[key] = value
    a['pk'] -> 1
    a['traffic_code'] -> "34 ABC 123"



    """