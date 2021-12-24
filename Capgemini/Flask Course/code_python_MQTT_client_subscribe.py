# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 16:34:12 2021

@author: anshu
"""

# MQTT subscribe client

import paho.mqtt.client as mq
c = mq.Client("4897612")
c.connect("test.mosquitto.org",1883)

def onc(c,userdata,flags,rc):
    print("Rc code is ",rc)
    c.subscribe("capegimini/today")

def onm(c,userdata,msg):
    print(msg.topic," : ",msg.payload.decode())
    
c.on_connect = onc
c.on_message = onm

c.loop_forever()