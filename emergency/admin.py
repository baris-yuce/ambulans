from django.contrib import admin
from .models import Ambulance, StationInfo, StandardEquipment

@admin.register(Ambulance)
class AmbulanceAdmin(admin.ModelAdmin):
    list_display = ('plate', 'traffic_code', 'ambulance_type', 'active', 'created_at')
    list_filter = ('ambulance_type', 'active')
    search_fields = ('plate', 'traffic_code')

@admin.register(StationInfo)
class StationInfoAdmin(admin.ModelAdmin):
    list_display = ('station_code', 'station_name', 'city', 'district', 'phone', 'active')
    list_filter = ('city', 'district', 'active')
    search_fields = ('station_code', 'station_name', 'city', 'district')

@admin.register(StandardEquipment)
class StandardEquipmentAdmin(admin.ModelAdmin):
    list_display = ('ambulance', 'main_stretcher', 'combination_stretcher', 'vacuum_stretcher')
    list_filter = ('main_stretcher', 'combination_stretcher', 'vacuum_stretcher')
    search_fields = ('ambulance__plate',)
