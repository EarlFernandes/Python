import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class First(unittest.TestCase):
    def test_first_Selenium_test(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://admin-demo.nopcommerce.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "Email").clear()
        self.driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
        #self.driver.find_element_by_id("user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "Password").clear()
        self.driver.find_element(By.ID, "Password").send_keys("admin")
        self.driver.find_element(By.XPATH, "//*[contains(@class, 'button-1 login-button')]").click()
        time.sleep(5)
        First.check_title(self)
        self.driver.quit()

    def check_title(self):
        Actual_title = self.driver.title
        Expected_title = "Dashboard / nopCommerce administration"
        if Actual_title == Expected_title:
            print ("Titles are same")
        else:
            print ("Titles are different, expected is " + Expected_title + " and retrived one is " + Actual_title)


