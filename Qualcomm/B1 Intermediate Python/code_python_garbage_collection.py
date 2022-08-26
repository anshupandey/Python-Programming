# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 12:18:48 2022

@author: admin
"""

# Garbage Collection

x = 5

del x

#####################################

import gc

i = 0
def get_some_garbage():
    x = {}
    x[i+1] = x
    print(x)
    
collected = gc.collect()
print(collected)

for i in range(10):
    get_some_garbage()
    
collected = gc.collect()
print(collected)
