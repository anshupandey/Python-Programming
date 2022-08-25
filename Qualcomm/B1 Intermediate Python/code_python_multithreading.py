# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 12:20:24 2022

@author: admin
"""

import threading
import time

def fun1():
    print("hey hii")
    time.sleep(3)
    print("good bye")
    
    
t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun1)
t3 = threading.Thread(target=fun1)  

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()