from django.contrib import admin
from .models import Ambulance, StationInfo, StandardEquipment

@admin.register(Ambulance)
class AmbulanceAdmin(admin.ModelAdmin):
    list_display = ('plate', 'ambulance_type', 'active', 'created_at')
    list_filter = ('ambulance_type', 'active')
    search_fields = ('plate', )

@admin.register(StationInfo)
class StationInfoAdmin(admin.ModelAdmin):
    list_display = ('station_code', 'station_name', 'city', 'city', 'phone', 'active')
    list_filter = ('city', 'neighborhood', 'active')
    search_fields = ('station_code', 'station_name', 'city', 'Neighborhood')

@admin.register(StandardEquipment)
class StandardEquipmentAdmin(admin.ModelAdmin):
    list_display = ('ambulance', 'main_stretcher', 'combination_stretcher', 'vacuum_stretcher')
    list_filter = ('main_stretcher', 'combination_stretcher', 'vacuum_stretcher')
    search_fields = ('ambulance__plate',)
