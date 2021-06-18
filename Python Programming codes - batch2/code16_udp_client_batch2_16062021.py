# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:29:58 2021

@author: Nitu
"""
# UDP Client
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(b"hey server, hope you are good",("127.0.0.1",12346))
data = s.recvfrom(2048)
print(data)