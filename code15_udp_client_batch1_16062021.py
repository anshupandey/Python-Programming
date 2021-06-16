# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 11:00:36 2021

@author: Nitu
"""
# UDP client

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(b"hi this is client", ("127.0.0.1",12347))
print(s.recvfrom(2048))