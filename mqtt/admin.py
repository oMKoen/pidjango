from django.contrib import admin

from .models import ModuleConfig, IoConfig, SensorConfig, ActorConfig, CommunicationConfig, Modules, Io, Sensor
from .Shellies.admin import *

# Register your models here.

@admin.register(ModuleConfig)
class ModuleConfigAdmin(admin.ModelAdmin):
    pass

@admin.register(IoConfig)
class IoConfigAdmin(admin.ModelAdmin):
    pass

@admin.register(SensorConfig)
class SensorConfigAdmin(admin.ModelAdmin):
    pass

@admin.register(ActorConfig)
class ActorConfigAdmin(admin.ModelAdmin):
    pass

@admin.register(CommunicationConfig)
class CommunicationConfigAdmin(admin.ModelAdmin):
    pass

@admin.register(Modules)
class ModulesAdmin(admin.ModelAdmin):
    pass

@admin.register(Io)
class IoAdmin(admin.ModelAdmin):
    pass

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    pass

