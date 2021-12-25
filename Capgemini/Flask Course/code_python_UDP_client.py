# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 15:35:13 2021

@author: anshu
"""

# UDP Client

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

host = "127.0.0.1"
port = 12346

server_add = (host,port)

s.sendto(b"Hello server, hope you are doing good today",server_add)
response = s.recvfrom(2048)
print(response)
s.close()

