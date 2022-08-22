from django.contrib import admin

from .models import ModuleConfig, IoConfig, SensorConfig, ActorConfig, Modules, Io, Sensor
# Register your models here.

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    pass

