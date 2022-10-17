from django.db import models

from .Shellies.models import *
# Create your models here.

# Base structure for Configurations
class ModuleConfig(models.Model):
    identifier = models.CharField(max_length=30)    #rolluik module/bewaterings esp
    version = models.CharField(max_length=30)
    config = models.TextField() #ioconfig identifier 

class IoConfig(models.Model):
    identifier = models.CharField(max_length=30)    #rolluik config
    version = models.CharField(max_length=30)
    config = models.TextField()

class SensorConfig(models.Model):
    identifier = models.CharField(max_length=30)    #button, dht22, limitswitch
    version = models.CharField(max_length=30)
    config = models.TextField() #hardware, software, communication

class ActorConfig(models.Model): 
    identifier = models.CharField(max_length=30)    #led, pump
    version = models.CharField(max_length=30)
    config = models.TextField()

class CommunicationConfig(models.Model):
    identifier = models.CharField(max_length=30)
    version = models.CharField(max_length=30)
    config = models.TextField()

# Create your models here.
class Modules(models.Model):
    identifier = models.CharField(max_length=30) 
    config = models.TextField()

class Io(models.Model):
    identifier = models.CharField(max_length=30)
    config = models.TextField()

class Sensor(models.Model):
    identifier = models.CharField(max_length=30)
    config = models.TextField()

    #dataType = models.CharField(max_length=30, default='default')
    #svalue = models.CharField(max_length=30, default='default')
    #tod = models.DateTimeField(auto_now=True)

class Actor(models.Model):
    identifier = models.CharField(max_length=30)
    config = models.TextField()
