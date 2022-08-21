import paho.mqtt.client as mqtt
from .models import Sensor
from . import IotModules
from decimal import *
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    
    client.subscribe("raspberry")
    
def on_message(client, userdata, msg):
    data = msg.payload.decode()
    print(f"{msg.topic} {str(data)}")
    
    try:
        data = json.loads(data)
    except:
        client.publish("rpi",f"invalid json received {msg.topic}: {data}")
        print("no json retrieved")
    else:

        client.publish("rpi",f"received {msg.topic}: {data}")
        if isinstance(data, dict) == True:
            print(f"dict detected: {type(data)}")
            for module in data:
                if IotModules.IotModulesCheck(module):    
                    for sensor in data[module]:
                        for read in data[module][sensor]:
                            print(f"add to database")
                            newEntry = Sensor(identifier=f"{module}_{sensor}", dataType=read, value=data[module][sensor][read])
                            newEntry.save()
        else:
            print(f"no dict detected: {type(data)}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)