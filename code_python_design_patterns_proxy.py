# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 14:55:01 2021

@author: anshu
"""

# =============================================================================
# Proxy = meaning of proxy - "in place of" OR "on behalf of"
# 
# =============================================================================

# creating a base class
class Video:
    def __init__(self,filename):
        self._filename = filename
        
    def load_video(self):
        print(f"Loading video  - {self._filename}")
        
    def display_video(self):
        print(f"Displaying video - {self._filename}")
        
# creating a base proxy class
class Proxy:
    def __init__(self,subject):
        self._subject = subject
        self._proxystate = None
        
# creating a proxy class for video class
class Proxyvideo(Proxy):
    def display_video(self):
        if self._proxystate==None:
            self._subject.load_video()
            self._proxystate = 1
        print(f"Loading video - {self._subject._filename}")
        
pv1 = Proxyvideo(Video("video1.mp4"))
pv2 = Proxyvideo(Video("video2.mp4"))

pv1.display_video()
pv2.display_video()        
    