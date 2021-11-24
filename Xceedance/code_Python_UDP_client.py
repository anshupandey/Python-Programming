# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:17:07 2021

@author: aspdi
"""


# UDP Client
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_add = ("127.0.0.1",12346)

s.sendto(b"hello server, from client",server_add)
response = s.recvfrom(2048)
print(response)