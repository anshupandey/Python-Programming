# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:58:38 2022

@author: admin
"""

class client:
    def __init__(self,sub):
        sub.subscribe(self)
        
    def notify(self,sub,*args,**kwargs):
        print("Got some message ",args,kwargs," from publisher ",sub)
    
        

class server:
    def __init__(self):
        self._subs = []
        
    def subscribe(self,client):
        self._subs.append(client)
        
    def notify_clients(self,*args,**kwargs):
        for obs in self._subs:
            obs.notify(self,*args,**kwargs)
            
    def unsubscribe(self,client):
        self._subs.remove(client)
        
    def __repr__(self):
        return "Publishing Server"
        
        
ser = server()

#creating two clients subscribing to ser
c1 = client(ser)
c1 = client(ser)

# send some message to the clients
ser.notify_clients("Hey Hi, how are you?",
                   sender="Anshu",age = 45)

ser.unsubscribe(c1)

ser.notify_clients("Hey Hi, how are you?",
                   sender="Anshu",age = 45)
