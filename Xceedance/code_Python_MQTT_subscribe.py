# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:45:12 2021

@author: aspdi
"""

import paho.mqtt.client as mq

c = mq.Client("4684")

c.connect("broker.hivemq.com",1883)

def onc(c,userdata,flags,rc):
    print("Rc code is ",rc)
    c.subscribe("mytopic/xceedance")
    
def onm(c,userdata,msg):
    print(msg.topic," : ",msg.payload.decode())
    
c.on_connect = onc
c.on_message = onm
c.loop_forever()