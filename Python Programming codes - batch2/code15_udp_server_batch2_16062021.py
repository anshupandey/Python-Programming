# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:27:05 2021

@author: Nitu
"""
# UDP Server

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = "127.0.0.1"
port = 12346
s.bind((host,port))
while True:
    data,address = s.recvfrom(2048)
    print(data," received from client ",address)
    s.sendto(b"Thans client",address)