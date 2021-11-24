# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 10:33:45 2021

@author: aspdi
"""

# TCP Client

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# send a connection request to the server
s.connect(('127.0.0.1',12345)) 

# receive data from the server
data = s.recv(1024)
print(data)
s.close()