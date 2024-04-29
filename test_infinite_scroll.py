# -*- coding: utf-8 -*-

"""
https://the-internet.herokuapp.com/infinite_scroll
"""

import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class TestInfiniteScroll(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.base_url = "https://the-internet.herokuapp.com/infinite_scroll"

    def test_infinite_scroll(self):
        driver = self.driver
        driver.get(self.base_url)
        title = driver.find_element(By.CSS_SELECTOR, '#content > div > h3')
        self.assertIn('Infinite Scroll', title.text)
        self.driver.save_full_page_screenshot('infinite-scroll-before.png')
        page = driver.find_element(By.TAG_NAME, 'html')
        before_scroll = len(driver.find_elements(By.CLASS_NAME, 'jscroll-added'))
        page.send_keys(Keys.END)
        time.sleep(3)
        after_scroll = len(driver.find_elements(By.CLASS_NAME, 'jscroll-added'))
        self.driver.save_full_page_screenshot('infinite-scroll-after.png')
        print(f"{after_scroll} > {before_scroll}")
        self.assertTrue(after_scroll > before_scroll)

    
    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


# Posted in https://github.com/AlihanFemi/Alihan 19:37