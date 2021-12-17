# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 11:11:55 2021

@author: anshu
"""

# Python - Chain of Responsibility
# =============================================================================
#  - used to build chain of objets
#  - allows an objct to send command to another
#  object without knowing who will handle the request
# =============================================================================

class AbstractHandler(object):
    def __init__(self,nxt):
        self._nxt = nxt
    def processRequest(self,request):
        raise NotImplementedError("Not implemented")
    def handle(self,request):
        handled = self.processRequest(request)
        if not handled:
            self._nxt.handle(request)
            
            
class FirstHandler(AbstractHandler):
    def processRequest(self, request):
        if 5 <request < 10:
            print(f"This is {self.__class__.__name__} handling the request {request}")
            return True

class SecondHandler(AbstractHandler):
    def processRequest(self, request):
        if 10 <request < 15:
            print(f"This is {self.__class__.__name__} handling the request {request}")
            return True

class ThirdHandler(AbstractHandler):
    def processRequest(self, request):
        if 15 <request < 20:
            print(f"This is {self.__class__.__name__} handling the request {request}")
            return True

class DefaultHandler(AbstractHandler):
    def processRequest(self, request):
        print(f"This is {self.__class__.__name__} handling the request {request}")
        return True

class user:
    def __init__(self):
        initial = None
        self.handler = FirstHandler(SecondHandler(ThirdHandler(DefaultHandler(initial))))
        
    def agent(self,user_request):
        for value in user_request:
            self.handler.handle(value)
            
            
user = user()
data = [5,6,8,7,9,10,12,15,18,19]        
user.agent(data)
