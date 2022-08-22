from django.http import HttpResponse, JsonResponse
#import paho.mqtt.client as mqtt 
from .models import Sensor


def index(request):
    
    data = list(Sensor.objects.filter(dataType="Temperature").values("tod", "svalue"))
    data = {"temperature": data}
    return JsonResponse(data, safe=False)

def IotData(request, iotmodule, sensor):
    data = list(Sensor.objects.filter(identifier=f"{iotmodule}_Sensor_{sensor}").values("tod", "dataType", "svalue"))
    
    data = {"iotmodule": {"d1": data[-1],"d2": data[-2]}}

    return JsonResponse(data, safe=False)
