import json

import select
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
        self.url = "http://localhost/signin.htm"
        self.driver.get(self.url)
        self.driver.find_element_by_id("signinUser").send_keys("zahraworker")
        self.driver.find_element_by_id("signinPassword").send_keys("12345w")

        self.driver.find_element_by_id("submintBtn")


        # self.user = User("zahra", "qweszxc20@yahoo.com", "5859831024820176", "09150394133", "1234567890")



    def test_transaction_unusual(self):
        assert "Worker Panel" in self.driver.title
        self.driver.find_element_by_id("transBtn").click()

        assert "Transactions Management" in self.driver.title
        select.select_by_index(1)# this is unusual transaction
        self.driver.find_element_by_id("report")
        self.driver.find_element_by_id("submitBtn").click()
        assert "Worker Panel" in self.driver.title
        self.driver.find_element_by_id("singoutBtn")
        assert "Home" in self.driver.title

        self.driver.find_element_by_id("signoutBtn").click()

        self.driver.find_element_by_id("singInButton").click()
        assert "singin page" in self.driver.title

        self.driver.find_element_by_id("signinUser").send_keys("admin")
        self.driver.find_element_by_id("signinPassword").send_keys("admin.admin")
        self.driver.find_element_by_id("submintBtn")
        assert "Manager Panel" in self.driver.title





    def tearDown(self):
        self.driver.close()
        self.assertTrue(True)

