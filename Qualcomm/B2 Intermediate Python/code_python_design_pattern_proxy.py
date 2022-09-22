# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:26:38 2022

@author: admin
"""

# Proxy - on behalf of someone

class video:
    def __init__(self,fname):
        self._fname = fname
        
    
    def load_video(self):
        print(f"Loading Video ... {self._fname}")
        
        
    def display_video(self):
        print(f"Displaying Video ... {self._fname}")
        

class proxybase:
    def __init__(self,subject):
        self._subject = subject
        self._proxystate=None
        
class proxyvideo(proxybase):
    def display_video(self):
        if self._proxystate==None:
            self._subject.load_video()
            self._proxystate = 1
        print(f"Displaying Video ... {self._subject._fname}")
        
        
pv1 = proxyvideo(video("video1.mp4"))
pv1.display_video()    


pv1.display_video()        
