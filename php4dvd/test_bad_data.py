# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Untitled2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled2(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_id("submit").click()
        self.assertEqual("This field is required", driver.find_element_by_css_selector("label.error").text)
        self.assertEqual("This field is required", driver.find_element_by_xpath("//form[@id='updateform']/table/tbody/tr[4]/td[2]/label").text)
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("bad")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_id("submit").click()
        self.assertEqual("This field is required", driver.find_element_by_xpath("//form[@id='updateform']/table/tbody/tr[4]/td[2]/label").text)
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("2015")
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        driver.find_element_by_id("submit").click()
        self.assertEqual("This field is required", driver.find_element_by_css_selector("label.error").text)
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_link_text("Log out").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
