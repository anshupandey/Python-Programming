# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:31:56 2021

@author: anshu
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common import keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://bandcamp.com/")
driver.find_element_by_class_name('play-btn').click()

time.sleep(10)
driver.close()

tracks = driver.find_elements_by_class_name('discover-item')
len(tracks)
tracks

# play 3rd song
tracks[7].click()

