# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 09:10:59 2021

@author: anshu
"""

# Selenium
# pip install selenium
# pip install webdriver-manager

# =============================================================================
# 1. open chrom browser
# 2. launch google.com
# 3. perform a search
# 4. close the browser
# 
# =============================================================================

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# opening the chrome browser
driver = webdriver.Chrome(ChromeDriverManager().install())
# maximize the chrom browser
driver.maximize_window()

driver.get("https://www.google.com/")
time.sleep(3)
# open the second tab
driver.execute_script("window.open('about:blank','secondtab');")
# switch to second tab
driver.switch_to.window('secondtab')
driver.get("https://www.python.org/")
time.sleep(5)
driver.close()

#############################################################
#############################################################

from selenium.webdriver.common.keys import Keys

# opening the chrome browser
driver = webdriver.Chrome(ChromeDriverManager().install())
# maximize the chrom browser
driver.maximize_window()

driver.get("https://www.google.com/")
time.sleep(2)
# find the search box element by name - 'q'
# type Xceedance into it
driver.find_element_by_name("q").send_keys("Xceedance")
time.sleep(1)
# click on the search button
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(5)
driver.close()


