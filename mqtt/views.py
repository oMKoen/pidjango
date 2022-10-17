from django.http import HttpResponse, JsonResponse
#import paho.mqtt.client as mqtt 
from .models import ModuleConfig, IoConfig,Sensor
import json


def index(request):
    
    data = list(Sensor.objects.filter(dataType="Temperature").values("tod", "svalue"))
    data = {"temperature": data}
    return JsonResponse(data, safe=False)

def IotData(request, iotmodule, sensor):
    data = list(Sensor.objects.filter(identifier=f"{iotmodule}_Sensor_{sensor}").values("tod", "dataType", "svalue"))
    
    data = {"iotmodule": {"d1": data[-1],"d2": data[-2]}}

    return JsonResponse(data, safe=False)

def modulesconfigall(request):
    modulesconfig = list(ModuleConfig.objects.values())

    return JsonResponse(modulesconfig, safe=False)

def modulesconfig(request, modulesconfig, version):
    if  version == None:
        queryset = list(ModuleConfig.objects.values())
        return JsonResponse(queryset, safe=False)
    else:
        query = list(ModuleConfig.objects.all().filter(identifier=modulesconfig, version=version).values())
        data = {}
        for queryset in query:
            for k in queryset:
                data[k] = (queryset[k])
            #idi = json.loads(queryset["config"])["IoConfig"]    #json.loads(queryset['config'])
            idi = data
            #IoQuery = list(IoConfig.objects.all().values())
        #query = list(ModuleConfig.objects.values())
        return JsonResponse(idi, safe=False)
    