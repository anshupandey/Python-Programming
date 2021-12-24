# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 15:23:33 2021

@author: anshu
"""
# TCP Client

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_add = "127.0.0.1"
server_port = 12345

# send connection request to the server
s.connect((server_add,server_port))

# receive data from server
data = s.recv(1024)
print(data)
s.close()