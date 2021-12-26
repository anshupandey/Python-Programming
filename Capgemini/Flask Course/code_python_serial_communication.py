# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 17:55:51 2021

@author: anshu
"""

# Python for serial communication
# hardware level transport layer protocol


# Serial communication with python - bluetooth

# step 1
# get a serial comm app in android device
# https://play.google.com/store/apps/details?id=de.kai_morich.serial_bluetooth_terminal&hl=en_IN&gl=US

# step 2
# pair your android device with windows pc

# step 3
# get the comport of bluetooth comm in your pc

# step 4
# get python client for bluetooth comm
# pip install pyserial


import serial

s.close()

s = serial.Serial("COM3")
print(s.name)

# open the app, accept the connection request
# 1. go to menu from top left corner
# 2. Devices
# 3. select your device (your pc)

# send data to the serial device - smartphone
s.write(b"hello hello, how are you \n")

# you should see the meesage on smartphone app

s.write(b"hii \n")

# to receive message
while True:
    data = s.readline()
    if data:
        print(data)