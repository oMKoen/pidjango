from django.db import models

# Base structure for Configurations
class ShellyConfig(models.Model):
    device_id = models.CharField(max_length=30)
    device_name = models.CharField(max_length=30)
    version = models.CharField(max_length=30)
    device_type = models.CharField(max_length=30)
    firmware_version = models.CharField(max_length=30)
    ip_address = models.CharField(max_length=20)
    mqtt_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now= True)
    
class Shelly2_5Config(models.Model):
    device_id = models.CharField(max_length=30)
    mode = models.CharField(max_length=30)
    relay_1_id = models.CharField(max_length=30)
    relay_2_id = models.CharField(max_length=30)
    roller_id = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now= True)

class Shelly2_5Relay_Config(models.Model):
    relay_id = models.CharField(max_length=30)
    appliance = models.CharField(max_length=30)
    appliance_id = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now= True)

class Shelly2_5Values(models.Model):
    device_id = models.CharField(max_length=30)
    input_0 = models.CharField(max_length=4)
    input_1 = models.CharField(max_length=4)
    temperature = models.CharField(max_length=5)
    overtemperature = models.CharField(max_length=10)
    temperature_status = models.CharField(max_length=10)
    voltage = models.CharField(max_length=5)
    timestamp = models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now= True)

class Shelly2_5RelayValues(models.Model):
    relay_id = models.CharField(max_length=30)
    longpush = models.CharField(max_length=4)
    input_event = models.CharField(max_length=10)
    relay = models.CharField(max_length=4)
    power = models.CharField(max_length=6)
    energy = models.CharField(max_length=6)
    overpower_value = models.CharField(max_length = 10)
    timestamp = models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now= True)

class Shelly2_5_RollerValues(models.Model):
    roller_id = models.CharField(max_length=30)
    roller = models.CharField(max_length=10)
    power = models.CharField(max_length=6)
    energy = models.CharField(max_length=6)
    position = models.CharField(max_length = 10)
    timestamp = models.DateTimeField(auto_now_add= True)
    updated= models.DateTimeField(auto_now= True)