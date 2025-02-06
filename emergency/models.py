from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Ambulance(models.Model):
    AMBULANCE_TYPES = [
        ('normal', 'Normal Ambulance'),
        ('intensive_care', 'Intensive Care Ambulance'),
        ('special', 'Specially Equipped Ambulance'),
    ]

    #traffic_code = models.CharField(max_length=10, verbose_name="Traffic Code")
    plate = models.CharField(max_length=10, unique=True, verbose_name="Plate")
    ambulance_type = models.CharField(max_length=20, choices=AMBULANCE_TYPES, verbose_name="Ambulance Type")
    active = models.BooleanField(default=True, verbose_name="Is Active?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ambulance"
        verbose_name_plural = "Ambulances"

    def __str__(self):
        return f"{self.plate} - {self.get_ambulance_type_display()}"

class StationInfo(models.Model):
    station_code = models.CharField(max_length=10, unique=True, verbose_name="Station Code")
    station_name = models.CharField(max_length=100, verbose_name="Station Name")
    
    # Detailed address information
    city = models.CharField(max_length=50, verbose_name="City")
    #district = models.CharField(max_length=50, verbose_name="District")
    neighborhood = models.CharField(max_length=100, verbose_name="Neighborhood")
    street = models.CharField(max_length=100, verbose_name="Street")
    building_no = models.CharField(max_length=20, verbose_name="Building No")
    floor = models.CharField(max_length=10, verbose_name="Floor", blank=True, null=True)
    postal_code = models.CharField(max_length=5, verbose_name="Postal Code")
    
    phone = models.CharField(max_length=11, verbose_name="Phone")
    ambulances = models.ManyToManyField(
        Ambulance, 
        related_name='stations', 
        verbose_name="Ambulances",
        blank=True
    )
    active = models.BooleanField(default=True, verbose_name="Is Active?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_address(self):
        return f"{self.neighborhood} Neighborhood, {self.street} Street, No:{self.building_no} {f'Floor:{self.floor}' if self.floor else ''} {self.Neighborhood}/{self.city}"

    class Meta:
        verbose_name = "Station Info"
        verbose_name_plural = "Station Information"

    def __str__(self):
        return f"{self.station_code} - {self.station_name}"

class StandardEquipment(models.Model):
    ambulance = models.OneToOneField(
        Ambulance, 
        on_delete=models.CASCADE, 
        related_name='standard_equipment',
        verbose_name="Ambulance"
    )
    main_stretcher = models.BooleanField(default=False, verbose_name="Main Stretcher")
    main_stretcher_count = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(5)],
        verbose_name="Main Stretcher Count"
    )
    combination_stretcher = models.BooleanField(default=False, verbose_name="Combination Stretcher")
    combination_stretcher_count = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(5)],
        verbose_name="Combination Stretcher Count"
    )
    vacuum_stretcher = models.BooleanField(default=False, verbose_name="Vacuum Stretcher")
    vacuum_stretcher_count = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(5)],
        verbose_name="Vacuum Stretcher Count"
    )
    scoop_stretcher = models.BooleanField(default=False, verbose_name="Scoop Stretcher")
    scoop_stretcher_count = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(5)],
        verbose_name="Scoop Stretcher Count"
    )
    spine_board = models.BooleanField(default=False, verbose_name="Spine Board")
    spine_board_count = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(5)],
        verbose_name="Spine Board Count"
    )
    traction_splint_set = models.BooleanField(default=False, verbose_name="Traction Splint Set")
    traction_splint_set_count = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(5)],
        verbose_name="Traction Splint Set Count"
    )
    inflatable_splint_set = models.BooleanField(default=False, verbose_name="Inflatable Splint Set")
    inflatable_splint_set_count = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(5)],
        verbose_name="Inflatable Splint Set Count"
    )
    cervical_collar_set = models.BooleanField(default=False, verbose_name="Cervical Collar Set")
    cervical_collar_set_count = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(5)],
        verbose_name="Cervical Collar Set Count"
    )
    ked_rescue_vest = models.BooleanField(default=False, verbose_name="KED Rescue Vest")
    ked_rescue_vest_count = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(5)],
        verbose_name="KED Rescue Vest Count"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Standard Equipment"
        verbose_name_plural = "Standard Equipment"

    def __str__(self):
        return f"Equipment List - {self.ambulance}"
