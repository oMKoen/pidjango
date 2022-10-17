from django.http import HttpResponse, JsonResponse
from .models import ShellyConfig, Shelly2_5Config
import json

import os


def modulesconfigall(request):
    shellyMqttModules = list(ShellyConfig.objects.values())

    return JsonResponse(shellyMqttModules, safe=False)

def shelly2_5moduleconfig(request):
    shelly2_5modules = list(Shelly2_5Config.objects.values())

    return JsonResponse(shelly2_5modules, safe=False)

def getAllSubscribeTopics(request):
    shellyMqttModules = list(ShellyConfig.objects.values('mqtt_id'))
    subscribe_topics_template = []
    subscribe_topics = []

    absolute_path = os.path.dirname(__file__)
    with open(f"{absolute_path}/templates/shelly2_5.json") as json_file:
        data_template = json.load(json_file)

    for modules in shellyMqttModules:
        data_module = data_template
        data_module['mqtt']['topic'] = modules['mqtt_id']

        subscribe_topics_template.append(data_module)
    
    return JsonResponse(subscribe_topics_template, safe=False)