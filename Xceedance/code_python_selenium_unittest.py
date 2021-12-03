# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:05:52 2021

@author: anshu
"""

import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class chromsearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_search_pythonorg(self):
        driver = self.driver
        driver.get("https://www.python.org/")
        self.assertIn("Python",driver.title)
        search_bar = driver.find_element_by_name("q")
        search_bar.send_keys("getting started with python")
        search_bar.send_keys(Keys.ENTER)
        url = "https://www.python.org/search/?q=getting+started+with+python&submit="
        assert url == driver.current_url
        
    def tearDown(self):
        self.driver.close()
        
if __name__=="__main__":
    unittest.main()
    
        
        