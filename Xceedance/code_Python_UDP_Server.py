# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:16:49 2021

@author: aspdi
"""

# UDP Server
import socket

s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

host = "127.0.0.1"
port = 12346

s.bind((host,port))

while True:
    data,addr = s.recvfrom(2048)
    print(data)
    s.sendto(b"Hey hi client, thanks for your data",addr)