import json
from selenium.webdriver.support.ui import Select

from selenium import webdriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Utils
from User import User


class SimpleTest(unittest.TestCase):

    def test_recharge(self):
        addreess = "http://mobadelan.herokuapp.com/Recharge"
        self.driver = webdriver.Chrome("/Users/fatemeh/Documents/Ap/chromedriver")
        self.driver.implicitly_wait(1)
        self.url = addreess
        self.driver.get(self.url)


        self.driver.find_element_by_id("walletvalue").send_keys(20000)
        self.driver.find_element_by_id("submitbtn").click()
        # self.user = User("zahra", "qweszxc20@yahoo.com", "5859831024820176", "09150394133", "1234567890")


    def test_signup(self):
        assert "Registration" in self.driver.title
        self.driver.find_element_by_id("emailid").send_keys("sa")
        self.driver.find_element_by_id("submitBtn").click()
        assert"Enter a valid email address." in self.driver.page_source

    def test_signup2(self):
        assert "Registration" in self.driver.title
        self.driver.find_element_by_id("phone_numberid").send_keys()
        self.driver.find_element_by_id("submitBtn").click()
        assert "This field is required." in self.driver.page_source


    def test_signup3(self):
        assert "Registration" in self.driver.title
        self.driver.find_element_by_id("usernameid").send_keys("f_sghee")
        self.driver.find_element_by_id("first_nameid").send_keys("ff")
        self.driver.find_element_by_id("last_nameid").send_keys("sghee")
        self.driver.find_element_by_id("emailid").send_keys("saghaei.zahra@yahoo.com")
        self.driver.find_element_by_id("phone_numberid").send_keys("02122222222")
        self.driver.find_element_by_id("bank_account_numberid").send_keys("89")
        self.driver.find_element_by_id("passwordid").send_keys("987654321Fs")
        self.driver.find_element_by_id("submitBtn").click()
        assert "exchange" in self.driver.page_source



