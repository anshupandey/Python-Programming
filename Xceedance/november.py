# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 11:06:39 2021

@author: anshu
"""

def myfun(a,b):
    return a+b


class A:
    x = 5
    y = 6
    def func1(self,a,*b):
        print("I am a function of class A")
        return a + sum(b)
    
    def func2(self):
        print("I am func2 , a function of class A")
        
        