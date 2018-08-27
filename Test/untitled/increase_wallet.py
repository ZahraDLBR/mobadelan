import json
from selenium.webdriver.support.ui import Select

from selenium import webdriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Utils
from User import User


class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.url = "http://localhost/signup.htm"
        self.driver.get(self.url)

        with open("info.json") as data_file:
            self.json = json.load(data_file)
        user = Utils.make_random_user()  # return a valid user
        self.driver.find_element_by_id("signUpButton").click()
        self.driver.find_element_by_id("myCheck").click()
        self.driver.find_element_by_id("submitBtn").click()

        self.driver.find_element_by_id("signupformname").send_keys(user.userName)
        self.driver.find_element_by_id("signupformbankacount").send_keys(user.bankAccount)
        self.driver.find_element_by_id("signupformemail").send_keys(user.e_mail)
        self.driver.find_element_by_id("signupformphonenumber").send_keys(user.phone)
        self.driver.find_element_by_id("signupformpassword").send_keys(user.password)
        self.driver.find_element_by_id("signupformrepassword").send_keys(user.password)
        self.driver.find_element_by_id("submit").click()
        # self.user = User("zahra", "qweszxc20@yahoo.com", "5859831024820176", "09150394133", "1234567890")

    def test_increase_wallet(self):
        assert "user panel" in self.driver.title
        self.driver.find_element_by_id("walletBtn").click()
        assert self.driver.find_element_by_id("walletvalue").text is "0"

        self.driver.find_element_by_id("managerwalletvalue").send_keys(self.json["exam"]["toefl"])
        self.driver.find_element_by_id("submitBtn").click()

        assert "increase wallet" in self.driver.title
        assert self.driver.find_element_by_id("walletvalue").text is self.json["exam"]["toefl"]
        self.driver.find_element_by_id("ok").click()

        assert "user panel" in self.driver.title



    def tearDown(self):
        self.driver.close()
        self.assertTrue(True)

