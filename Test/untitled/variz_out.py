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

        self.user = user
        # self.user = User("zahra", "qweszxc20@yahoo.com", "5859831024820176", "09150394133", "1234567890")

    def increase_wallet(self, value):
        assert "user panel" in self.driver.title
        self.driver.find_element_by_id("walletBtn").click()
        self.driver.find_element_by_id("managerwalletvalue").send_keys(value)
        self.driver.find_element_by_id("submitBtn").click()
        self.driver.find_element_by_id("ok").click()
        assert "user panel" in self.driver.title

    def test_register_exam(self):

            self.increase_wallet(30000)
            self.driver.find_element_by_id("paymentBtn").click()
            assert "payment" in self.driver.title
            self.driver.find_element_by_id("varizOutBtn").click()
            self.driver.find_element_by_id("pay6hesabmaghsad").send_keys(self.user.bankAccount)
            self.driver.find_element_by_id("pay6varizi").send_keys(14000)
            self.driver.find_element_by_id("submitBtn").click()
            #commission
            assert "commission" in self.driver.title
            assert self.driver.find_element_by_id("commission").text is self.json["commission"]["varizOut"]*20000

            self.driver.find_element_by_id("submitBtn").click()
            WebDriverWait(self.driver, 3).until(EC.alert_is_present(),
                                                'Timed out waiting for PA creation ' +
                                                'confirmation popup to appear.')

            alert = self.driver.switch_to.alert
            alert.accept()

            assert "receipt" in self.driver.title
            assert "درخواست شما با موفقیت ثبت شد منتظر تایید از سمت موسسه باشید." in self.driver.page_source
            self.transactionNum  = self.driver.find_element_by_id("transactionNum").text
            self.driver.find_element_by_id("ok").click()

            assert "user panel" in self.driver.title
            self.driver.find_element_by_id("transactionBtn").click()
            assert "transactions" in self.driver.title
            assert "منتظر تایید" in self.driver.find_element_by_id(self.transactionNum).text


    def test_bad(self):
        self.driver.find_element_by_id("paymentBtn").click()
        assert "payment" in self.driver.title
        self.driver.find_element_by_id("varizOutBtn").click()
        self.driver.find_element_by_id("pay6hesabmaghsad").send_keys(self.user.bankAccount)
        self.driver.find_element_by_id("pay6varizi").send_keys(34000)
        self.driver.find_element_by_id("submitBtn").click()

        assert "please charge you wallet and try again" in self.driver.page_source

    def test_bad2(self):
        self.driver.find_element_by_id("paymentBtn").click()
        assert "payment" in self.driver.title
        self.driver.find_element_by_id("varizOutBtn").click()
        self.driver.find_element_by_id("pay6hesabmaghsad").send_keys(self.user.bankAccount)
        self.driver.find_element_by_id("pay6varizi").send_keys(150)
        self.driver.find_element_by_id("submitBtn").click()

        assert "you must enter value more than 10000" in self.driver.page_source


    def test_bad3(self):
        self.driver.find_element_by_id("paymentBtn").click()
        assert "payment" in self.driver.title
        self.driver.find_element_by_id("varizOutBtn").click()
        self.driver.find_element_by_id("pay6hesabmaghsad").send_keys(self.user.bankAccount)
        self.driver.find_element_by_id("pay6varizi").send_keys(150000000000)
        self.driver.find_element_by_id("submitBtn").click()

        assert "you must enter value less than 10000000" in self.driver.page_source

    def tearDown(self):
        self.driver.close()
        self.assertTrue(True)

