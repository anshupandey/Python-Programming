# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 16:07:25 2021

@author: anshu
"""

#MQTT
# broker implementation (open) - Mosquitto, Mosca
# client - paho
# pip install paho-mqtt

# MQTT Client - publish

# Broker - broker.hivemq.com

import paho.mqtt.client as mq
import time

broker = "test.mosquitto.org"

port = 1883
client = mq.Client("4315846453")
client.connect(broker,port)
time.sleep(1)
msg = input("Enter your message: ")
client.publish("capegimini/today",str(msg),retain=True)
client.disconnect()

