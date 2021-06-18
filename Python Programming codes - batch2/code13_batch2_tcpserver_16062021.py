# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:53:05 2021

@author: Nitu
"""

# TCp Server
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# AF_INET = addressing family of underlying networking protocol,
# AF_INET = IPv4 address formatting will be used for this socket
# SOCK_STREAM = communication type = TCP
host = "127.0.0.1"
port = 12345
s.bind((host,port))

s.listen(5) # keep 5 connection active 
while True:
    ts,addr = s.accept()
    # ts = temporary socket assigned to client
    # addr = address of the client which has sent the request
    print("Request received from client ",addr)
    ts.send(b"Hey hi client thank you for connection")
    ts.close()
    
    
    
    
    
    
    
    
    
    
    
    