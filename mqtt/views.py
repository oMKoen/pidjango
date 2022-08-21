from django.http import HttpResponse, JsonResponse
#import paho.mqtt.client as mqtt 
from .models import Sensor


def index(request):
    
 #   client = mqtt.Client()
 #   client.connect("127.0.0.1", 1883, 60)
 #   client.publish("rpi","alli baba loves kebab")
  data = list(Sensor.objects.filter(dataType="Temperature").values("tod", "value"))
  data = {"temperature": data}
  return JsonResponse(data, safe=False)