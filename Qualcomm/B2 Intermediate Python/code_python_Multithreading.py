# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 14:52:39 2022

@author: admin
"""

import threading
import time 

def myfun():
    print("Hey good morning")
    time.sleep(4)
    print("THanks bye")
    
    
t1 = threading.Thread(target=myfun)
t2 = threading.Thread(target=myfun)
t1.start()
t2.start()

t1.join() # wait for the thread to complete unless it is executed completely
t2.join()
