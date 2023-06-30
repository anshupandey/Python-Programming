# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 11:40:00 2022

@author: admin
"""

# =============================================================================
# Proxy - on behalf of another class creating a new class
# =============================================================================


class video:
    def __init__(self,filename):
        self._filename = filename 
        
    def load_video(self):
        print("Loading video ",self._filename)
        
    def display_video(self):
        print("Displaying video ",self._filename)



#  creating a base proxy class
class proxy:
    def __init__(self,subj):
        self._sub = subj
        self._proxystate = None
   
# creating a proxy class for video

class proxyVideo(proxy):
    
    def display_video(self):
        if self._proxystate ==None:
            self._sub.load_video()
            self._sub.display_video()
            self._proxystate = 1
        print(f"Loading video : {self._sub._filename}")
        
        
pv1 = proxyVideo(video("video1.mp4"))
pv2 = proxyVideo(video("video2.mp4"))

pv1.display_video()

pv2.display_video()
