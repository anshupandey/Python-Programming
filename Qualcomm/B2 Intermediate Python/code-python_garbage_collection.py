# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 15:48:47 2022

@author: admin
"""

# Grabage Collection

x = 5
del x

###############################

x = 5
id(x)
y = 5
id(y)

x = 9
id(x)

m = 5
id(m)


del x
del y
del m
k = 5
id(k)


#####################################################

import gc
collected = gc.collect()
print(collected)


collected = gc.collect()
print(collected)


i = 0
def create_garbage():
    x = {}
    x[i+1] = x
    print(x)

collected = gc.collect()
print(collected)

for i in range(10):
    create_garbage()

collected = gc.collect()
print(collected)

    