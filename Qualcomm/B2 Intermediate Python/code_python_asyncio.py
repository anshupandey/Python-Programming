# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 14:31:52 2022

@author: admin
"""

import asyncio 
import time

async def greet(text):
    await asyncio.sleep(3)
    print(text)

g = greet("hi")
type(g)

# await g  

async def main():
    task1 = asyncio.create_task(greet("Hello World"))
    task2 = asyncio.create_task(greet("Bye World"))
    print("Start time: ",time.ctime())
    await task1
    await task2
    print("Stop time: ",time.ctime())
    
asyncio.run(main())
