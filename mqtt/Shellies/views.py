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

def getAllShellySubscribeTopics(request):
    shellyMqttModules = list(ShellyConfig.objects.values('device_id', 'mqtt_id'))
    subscribe_topics_template = []
    subscribe_topics = []

    absolute_path = os.path.dirname(__file__)
    with open(f"{absolute_path}/templates/shelly2_5.json") as json_file:
        data_template = json.load(json_file)

    for modules in shellyMqttModules:
        shelly2_5 = list(Shelly2_5Config.objects.values().filter(device_id =  modules['device_id']))

        data_module = data_template
        data_module['mqtt']['topic'] = modules['mqtt_id']
        for subtopic in data_module['mqtt']['subscribe']['subtopic']['general']:
            subscribe_topics.append(subtopic)

        for subtopic in data_module['mqtt']['subscribe']['subtopic'][shelly2_5[0]['mode']]:
            subscribe_topics.append(subtopic)
    
    return JsonResponse(subscribe_topics, safe=False)

def getShellySubscribeTopics():
    shellyMqttModules = list(ShellyConfig.objects.values('device_id', 'mqtt_id'))
    subscribe_topics_template = []
    subscribe_topics = []

    absolute_path = os.path.dirname(__file__)
    with open(f"{absolute_path}/templates/shelly2_5.json") as json_file:
        data_template = json.load(json_file)

    for modules in shellyMqttModules:
        shelly2_5 = list(Shelly2_5Config.objects.values().filter(device_id =  modules['device_id']))

        data_module = data_template
        data_module['mqtt']['topic'] = modules['mqtt_id']
        for subtopic in data_module['mqtt']['subscribe']['subtopic']['general']:
            subscribe_topics.append(f"{data_module['mqtt']['topic']}/{subtopic}")

        for subtopic in data_module['mqtt']['subscribe']['subtopic'][shelly2_5[0]['mode']]:
            subscribe_topics.append(f"{data_module['mqtt']['topic']}/{subtopic}")
    
    return subscribe_topics