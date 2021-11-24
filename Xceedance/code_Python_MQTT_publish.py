# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:45:00 2021

@author: aspdi
"""

# pip install paho-mqtt

import paho.mqtt.client as mq

broker = "broker.hivemq.com"
port = 1883
client = mq.Client("aiifekfgou") # creating a client isntance
# connect to broker
client.connect(broker,port)
client.publish("mytopic/xceedance","hi from Anshu..")
