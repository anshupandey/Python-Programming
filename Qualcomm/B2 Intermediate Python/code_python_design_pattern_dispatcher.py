# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:45:34 2022

@author: admin
"""

from multipledispatch import dispatch

# dispatch helps in selection of process/method based on types, signature

@dispatch(int)
def myfun(a):
    return a**2



@dispatch(float)
def myfun(a):
    return a**3



myfun(6)
myfun(6.0)
