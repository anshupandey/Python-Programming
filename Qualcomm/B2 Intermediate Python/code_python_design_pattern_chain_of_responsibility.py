# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:26:20 2022

@author: admin
"""

# =============================================================================
# CHain of Responsibility
# 
#     - allows the object to send commands to other
#     - building a chain of objects
#     
# =============================================================================


class AbstractHandler(object):
    def __init__(self,nxt):
        self._nxt = nxt
        
    def processRequest(self,request):
        raise NotImplementedError("This situtaion for data is not implemented")
        
    def handle(self,request):
        handled = self.processRequest(request)
        if not handled:
            self._nxt.handle(request)
            
            

class FirstHandler(AbstractHandler):
    def processRequest(self,request):
        if request<18:
            print(f"this is {self.__class__.__name__} handling the request {request}")
            return True
        

class SecondHandler(AbstractHandler):
    def processRequest(self,request):
        if request>=18 and request<30:
            print(f"this is {self.__class__.__name__} handling the request {request}")
            return True


class ThirdHandler(AbstractHandler):
    def processRequest(self,request):
        if request>=30 and request<60:
            print(f"this is {self.__class__.__name__} handling the request {request}")
            return True
        
class DefaultHandler(AbstractHandler):
    def processRequest(self,request): 
        print(f"this is {self.__class__.__name__} handling the request {request}")
        return True


class user:
    def __init__(self):
        self.initial = None
        self.handler = FirstHandler(SecondHandler(ThirdHandler(DefaultHandler(self.initial))))
        
    def agent(self,data):
        for val in data:
            self.handler.handle(val)

        

u = user()
age = [12,18,15,25,23,54,33,65,41]
u.agent(age)
