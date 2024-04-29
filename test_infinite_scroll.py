# -*- coding: utf-8 -*-

"""
https://the-internet.herokuapp.com/infinite_scroll
"""

import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class TestDragAndDrop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.base_url = "https://the-internet.herokuapp.com/infinite_scroll"

    def test_drag_drop(self):
        driver = self.driver
        driver.get(self.base_url)
        drag = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#column-a')))
        drop = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#column-b')))
        self.driver.save_full_page_screenshot('dag-before.png')
        ActionChains(driver).drag_and_drop(drag, drop).perform()
        time.sleep(3)
        self.driver.save_full_page_screenshot('dag-after.png')
        test = driver.find_element(By.CSS_SELECTOR, '#column-a > header')
        self.assertTrue('B', test.text)
    
    
    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
