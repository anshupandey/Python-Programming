# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 15:14:59 2021

@author: anshu
"""
# =============================================================================
# 
# TCP
#  - connecttion oriented protocol
#  - client needs to connect to server to start exchanging data
#  - http, mqtt, smtp, imap
#
#  
# UDP
#  - connectionless protocol
#  - no continuous connection needed to start exchanging data
#  - VOIP, CoAP
# =============================================================================


import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket.AF_INET = socket family, IPv4 addressing
# socket.SOCK_STREAM = TCP based communication

host = "127.0.0.1"
port = 12345

s.bind((host,port))

s.listen(5)

while True:
    ts,addr = s.accept()
    print("Got a conection request from client ",addr)
    # respond to the client
    ts.send(b"Hey hi client, thanks for your message")
    ts.close()