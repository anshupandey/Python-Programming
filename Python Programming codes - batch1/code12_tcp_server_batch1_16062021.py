# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 09:04:30 2021

@author: Nitu
"""
# TCP Server

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# AF_INET = socket family = for IPv4 address formatting
# SOCK_STREAM = TCP based communication

host = '127.0.0.1'
port = 12345

s.bind((host,port))

s.listen(5) # wait for connections, 5 clients in wait

while True:
    ts,addr = s.accept()
    # ts = temporary socket assigned to the client for the communication
    # addr = address of the client who sent the request
    print("got a connection request from ",addr)
    
    ts.send(b"Thank you for sending the request, here is your data - hi")
    ts.close()