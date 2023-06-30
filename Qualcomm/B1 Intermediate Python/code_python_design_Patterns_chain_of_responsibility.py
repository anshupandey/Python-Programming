# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 10:37:45 2022

@author: admin
"""

# =============================================================================
# Chain of responsibility
# - chaiing the objects together, handling exceptions
# =============================================================================



class AbstractHandle(object):
    def __init__(self,nxt_h):
        self._next = nxt_h
    def processRequest(self,request):
        raise NotImplementedError("not implemented")
        
    def handle(self,request):
        handled = self.processRequest(request)
        if not handled:
            self._next.handle(request)
            
class FirstHandler(AbstractHandle):
    def processRequest(self, request):
        if request<18:
            print(f"This request is handled by {self.__class__.__name__}, thre request value is {request}")
            return True
            
class SecondHandler(AbstractHandle):
    def processRequest(self, request):
        if request>=18 and request<30:
            print(f"This request is handled by {self.__class__.__name__}, thre request value is {request}")
            return True

class ThirdHandler(AbstractHandle):
    def processRequest(self, request):
        if request>=30 and request<60:
            print(f"This request is handled by {self.__class__.__name__}, thre request value is {request}")
            return True
            
class DefaultHandler(AbstractHandle):
    def processRequest(self, request):
        print(f"This request is handled by {self.__class__.__name__}, thre request value is {request}")
        return True

            
class user:
    def __init__(self):
        initial = None
        self.handler = FirstHandler(SecondHandler(ThirdHandler(DefaultHandler(initial))))
        
    def agent(self,data):
        for val in data:
            self.handler.handle(val)
            
            
u = user()
dd = [12,15,45,32,65,25,35,18,11]
u.agent(dd)
