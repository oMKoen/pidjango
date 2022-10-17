from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(ShellyConfig)
class ShellyConfigAdmin(admin.ModelAdmin):
    pass

@admin.register(Shelly2_5Config)
class Shelly2_5ConfigAdmin(admin.ModelAdmin):
    pass

@admin.register(Shelly2_5Relay_Config)
class Shelly2_5Relay_ConfigAdmin(admin.ModelAdmin):
    pass

@admin.register(Shelly2_5Values)
class Shelly2_5ValuesAdmin(admin.ModelAdmin):
    pass

@admin.register(Shelly2_5RelayValues)
class Shelly2_5RelayValuesAdmin(admin.ModelAdmin):
    pass

@admin.register(Shelly2_5_RollerValues)
class Shelly2_5_RollerValuesAdmin(admin.ModelAdmin):
    pass

