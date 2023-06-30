import paho.mqtt.client as mq
import time

c = mq.Client()
c.connect("broker.hivemq.com")
time.sleep(1)

def onc(client,userdata,flags,rc):
    print("connected to broker with rc code ",0)
    c.subscribe("mytopic/today")
    c.subscribe("factory/machine1")

def onm(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

c.on_connect = onc
c.on_message = onm
c.loop_forever()