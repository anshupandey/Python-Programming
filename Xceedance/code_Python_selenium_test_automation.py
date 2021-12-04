# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 10:15:15 2021

@author: anshu
"""

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys

# opening the chrome browser
driver = webdriver.Chrome(ChromeDriverManager().install())
# maximize the chrom browser
driver.maximize_window()

driver.get("https://www.youtube.com/")
time.sleep(2)
# find the search box element by name - 'q'
# type Xceedance into it
driver.find_element_by_name("search_query").send_keys("python")
time.sleep(1)
# click on the search button
driver.find_element_by_id("search-icon-legacy").send_keys(Keys.ENTER)
time.sleep(5)
driver.close()

#################################################################

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys


# opening the chrome browser
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.python.org/")
time.sleep(2)

print(driver.title)

search_bar = driver.find_element_by_name('q')
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.ENTER)

print(driver.current_url)

time.sleep(5)
driver.close()