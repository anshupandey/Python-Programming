# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 10:56:04 2021

@author: Nitu
"""

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = "127.0.0.1"
port = 12347
s.bind((host,port))

while True:
    data,addr = s.recvfrom(2048)
    print(data)
    s.sendto(b"hey hi client",addr)