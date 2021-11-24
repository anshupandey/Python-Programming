# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 10:23:40 2021

@author: aspdi
"""

# TCP Server

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# SF_INET = scoket family = for IPv4 addressing
# SOCK_STREAM = TCP based communication

host = "127.0.0.1"
port = 12345

s.bind((host,port)) # binding the host address and port to the socket

s.listen(5) # wait for connections

while True:
    ts,addr = s.accept()
    # ts = a temporary socket assigned to the client for communication
    # addr = address of the client
    print("Got a connection request from client, ",addr)
    #respond to the client
    ts.send(b"Hey hi client, thanks for requesting data - here is your data - hi")
    ts.close()