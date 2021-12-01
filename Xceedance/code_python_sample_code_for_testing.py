# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 11:23:30 2021

@author: aspdi
"""

def add(a,b):
    "this is to add two numbers"
    return a+b

def subtract(a,b):
    "this to subtract a number from other"
    return a-b

def multiply(a,b):
    """ THis function multiplies two numbers
       Parameters
    ----------
    a : int/float
    b : int/float
    Returns
    -------
    float
    
    >> multiply(4,5)
    >> 20.0
    >> multiple(4,8)
    >> 32.0
    """
    return float(a*b)

def divide(a,b):
    "this function divides a number by other"
    if b==0:
        raise ValueError("can not divide by zero")
    return a/b
