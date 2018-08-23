# encoding: utf-8
from __future__ import unicode_literals

import datetime
import json
import subprocess
import RPi.GPIO as GPIO
import time

import paho.mqtt.client as mqtt

fromtimestamp = datetime.datetime.fromtimestamp

# MQTT client to connect to the bus
mqtt_client = mqtt.Client()
HOST = "localhost"
PORT = 1883
HOTWORD_DETECTED = "hermes/hotword/default/detected"
HOTWORDS_ON = {"lumos"}
HOTWORDS_OFF = {"nocte"}
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm1=GPIO.PWM(11,60)
pwm1.start(0)

# Subscribe to the important messages
def on_connect(client, userdata, flags, rc):
    mqtt_client.subscribe(HOTWORD_DETECTED)


# Process a message as it arrives
def on_message(client, userdata, msg):
    if not msg.topic == HOTWORD_DETECTED:
        return

    payload = json.loads(msg.payload)
    model_id = payload["modelId"]
    if model_id in HOTWORDS_ON:
        for x in range(1, 100)
            pwm1.ChangeDutyCycle(x)
            sleep(.25)
            print x
    elif model_id in HOTWORDS_OFF:
        for x in range(100, 1)
            pwm1.ChangeDutyCycle(x)
            sleep(.25)
            print x
    else:
        print("Unmapped hotword model_id: %s" % model_id)


if __name__ == '__main__':
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(HOST, PORT)
    mqtt_client.loop_forever()
