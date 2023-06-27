import time
import unittest
from selenium import webdriver

class First(unittest.TestCase):
    def test_first_Selenium_test(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.driver.find_element_by_id("user-name").send_keys("standard_user")
        self.driver.find_element_by_id("password").send_keys("secret_sauce")
        self.driver.find_element_by_id("login-button").click()
        time.sleep(5)
        First.check_title(self)
        self.driver.quit()

    def check_title(self):
        Actual_title = self.driver.title
        Expected_title = "Swag Labs"
        if Actual_title == Expected_title:
            print ("Titles are same")
        else:
            print ("Titles are different, expected is " + Expected_title + " And retrived is " + Actual_title)


