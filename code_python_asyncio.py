# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 11:30:01 2021

@author: anshu
"""

import asyncio

def greet():
    return "Hey Good morning"

greet()

async def greet():
    return "Hey good morning"

gr = greet()
type(gr)

##################################

async def main():
    await asyncio.sleep(4)
    return "hello world form Python"

asyncio.run(main())
