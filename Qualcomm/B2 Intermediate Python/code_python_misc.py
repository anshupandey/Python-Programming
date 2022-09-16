# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 16:03:53 2022

@author: admin
"""

import inspect
import asyncio

class A:
    x = 5
    def myfun(self):
        print("class A")
        
class B(A):
    y = 6
    def myfun2(self):
        print("class B")
        
        
def greet(a,b):
    "hi this is doc"
    print("hello world0")
    return a+b

    
async def fun2():
    await asyncio.sleep(3)
    print("hello world")
    
f = fun2()


inspect.isclass(greet)
inspect.isclass(A)
inspect.isfunction(greet)
inspect.isclass(B)
inspect.isasyncgen(f)
inspect.getdoc(greet)
inspect.getmro(B)
inspect.getmro(A)
inspect.getmembers(A)

greet(4,5)


###############################################


# traceback

import traceback
import sys

a = [4,5,3]

try:
    out = a[9]
except Exception as e:
    traceback.print_exc()
    print(e)
    exc_type, exc_value, exc_tb = sys.exc_info()
    print("Error occured on line ",exc_tb.tb_lineno)
    print("Exception text ",exc_tb.tb_next)
    
    
########################################################
# Code Profiling


import time

def fun2():
    start = time.time()
    print("function running up")
    stop = time.time()
    print("this function took ",stop-start, " seconds")
    
    
fun2()

# cProfile

import cProfile

cProfile.run("10+10")
##################################

import cProfile, io, pstats
from pstats import SortKey
ob = cProfile.Profile()

ob.enable()

m = 45**65466

ob.disable()
print(ob)

sec = io.StringIO()
ps = pstats.Stats(ob,stream=sec).sort_stats(SortKey.CUMULATIVE)

ps.print_stats()
print(sec.getvalue())


#############################


import timeit

setupcode = "from math import sqrt"

code = """
def myfun():
    nlist = []
    for i in range(10):
        nlist.append(sqrt(i))
"""

print(timeit.timeit(setup = setupcode, stmt=code,
                    number=100))