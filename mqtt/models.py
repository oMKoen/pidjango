#import django
#django.setup()
from django.db import models

# Create your models here.
class Sensor(models.Model):
    identifier = models.CharField(max_length=30)
    dataType = models.CharField(max_length=30, default='default')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    tod = models.DateTimeField(auto_now=True)