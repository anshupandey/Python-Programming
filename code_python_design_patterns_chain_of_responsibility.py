# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 15:25:32 2021

@author: anshu
"""

# Python Design Pattern
# Chain of responsibility

# - used to build chain of objets, allows an object to send command to another
# object without knowing who is going to handle the request


class AbstractHandler(object):
    def __init__(self,nxt):
        self._next = nxt
        
    def processRequest(self,request):
        raise NotImplementedError("this method is yet to be implemented")
        
    def handle(self,request):
        handled = self.processRequest(request)
        if not handled:
            self._next.handle(request)
            
            

class FirstEventHandler(AbstractHandler):
    def processRequest(self, request):
        if 5 < request < 10:
            print(f"this is {self.__class__.__name__} handling the request - {request}")
            return True

class SecondEventHandler(AbstractHandler):
    def processRequest(self, request):
        if 10 < request < 15:
            print(f"this is {self.__class__.__name__} handling the request - {request}")
            return True

class ThirdEventHandler(AbstractHandler):
    def processRequest(self, request):
        if 15 < request < 20:
            print(f"this is {self.__class__.__name__} handling the request - {request}")
            return True

class DefaultEventHandler(AbstractHandler):
    def processRequest(self, request):
        print(f"this is {self.__class__.__name__} handling the request - {request}")
        return True
        
class user:
    def __init__(self):
        initial = None
        self.handler = FirstEventHandler(SecondEventHandler(ThirdEventHandler(DefaultEventHandler(initial))))
        
    def agent(self,user_request):
        for val in user_request:
            self.handler.handle(val)
            
            
        
user = user()
mydata = [4,5,6,9,8,7,10,12,15,18,11,20,14]
user.agent(mydata)
