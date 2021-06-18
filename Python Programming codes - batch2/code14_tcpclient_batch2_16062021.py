# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:59:27 2021

@author: Nitu
"""
# TCP Client

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connect to the server
s.connect(("127.0.0.1",12345))
data = s.recv(1024)
print(data)
s.close()