# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 11:56:22 2022

@author: admin
"""

import asyncio

def greet():
    return "hey Good morning"



async def greet():
    return "Hey good moning"

gr = greet()
type(gr)

#await gr

###################################################

async def greet():
    print("hey hi")
    await asyncio.sleep(3)
    print("Hey good morning")

######################################################

##############################################################
import time
import asyncio

async def greet():
    print("hey hi")
    await asyncio.sleep(3)
    print("Hey good morning")


async def main():
    task1 = asyncio.create_task(greet())
    task2 = asyncio.create_task(greet())
    print("start time ",time.ctime())
    await task1
    await task2
    print("stop time ",time.ctime())


asyncio.run(main())




















