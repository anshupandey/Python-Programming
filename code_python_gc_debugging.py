# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 11:34:35 2021

@author: anshu
"""

x = [4,5,6]

del x

# AUtomatic Garbage collection
# threshold < number of object allocation - number of deallocations

import gc
print('Garbafe collection threshold ',gc.get_threshold())


# manual garbage collection

collected = gc.collect()

print(collected)


#####################################################
##################################################

# using inspect module

import inspect

class A:
    x = 5
    def myfun(self):
        print("class A")
        
class B(A):
    y = 6
    def myfun2(self):
        print("class B")
        
        
k = B()

def hello():
    print("hi")
    
async def hello2():
    print("hi")

inspect.isclass(A)
inspect.isfunction(hello)
inspect.isasyncgen(hello)

inspect.getmro(B)


###################################################

import traceback

import sys
A = [1,2,5,8,5]

try:
    value = A[9]
except:
    traceback.print_exc()
    exc_type,exc_value,exc_tb = sys.exc_info()
    print(exc_tb.tb_lineno)
    print(exc_tb.tb_next)
    