# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 16:02:31 2021

@author: anshu
"""

x = [4,5,6,3]
del x

print(x)


import gc

# automated garbage collection
# threshold > number of allocation - number of deallocations

print(gc.get_threshold())


# manual garbage collection

collected= gc.collect()
print(collected)


###########################################

i = 0

def create_garbage():
    x = {}
    x[i+1] = x
    print(x)
    
collected= gc.collect()
print(collected)

for i in range(10):
    create_garbage()
    
    
collected= gc.collect()
print("collected ",collected," objects")
    