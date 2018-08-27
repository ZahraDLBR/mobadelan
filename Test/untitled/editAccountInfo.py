from selenium import webdriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Utils


class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.url = "http://localhost/signup.htm"
        self.driver.get(self.url)

        user = Utils.make_random_user() # return a valid user
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
        self.driver.find_element_by_id("accountBtn").click()
        self.driver.find_element_by_id("editBtn").click()
        assert "edit" in self.driver.title

        self.new_user = user

    def test_bad_edit_account_info(self):

        self.driver.find_element_by_id("editinfoname").send_keys("zahra")
        self.driver.find_element_by_id("editinfopassword").send_keys("1234567")
        self.driver.find_element_by_id("editinforepassword").send_keys("1234567")
        self.driver.find_element_by_id("editinfobankaccount").send_keys("1111111")#incorrect
        self.driver.find_element_by_id("editinforepassword").send_keys("1234567")

        self.driver.find_element_by_id("submitBtn").click()
        assert "edit" in self.driver.title
        assert "pleas enter a valid back account number" in self.driver.page_source


    def test_good_edit_account_info(self):

        self.driver.find_element_by_id("editinfopassword").send_keys("1234567")
        self.driver.find_element_by_id("editinforepassword").send_keys("1234567")
        self.driver.find_element_by_id("editinfobankaccount").send_keys("5859831024823176")  # incorrect
        self.driver.find_element_by_id("editinforepassword").send_keys("1234567")
        self.driver.find_element_by_id("editinfocheckbox3").click()

        self.driver.find_element_by_id("submitBtn").click()
        WebDriverWait(self.driver, 3).until(EC.alert_is_present(),
                                        'Timed out waiting for PA creation ' +
                                        'confirmation popup to appear.')

        alert = self.driver.switch_to.alert
        alert.accept()

        assert "account information" in self.driver.title
        assert self.driver.find_element_by_id("bankaccount") is "5859831024823176"
        assert self.driver.find_element_by_id("notif") is "phone"

        self.driver.find_element_by_id("returnBtn").click()
        assert "user panel" in self.driver.title
        self.driver.find_element_by_id("signoutBtn").click()
        assert "main page" in self.driver.title
        self.driver.find_element_by_id("signInButton").click()

        assert "singin page" in self.driver.title
        self.driver.find_element_by_id("signinUser").send_keys(self.new_user.userName)
        self.driver.find_element_by_id("signinPassword").send_keys(self.new_user.password)
        self.driver.find_element_by_id("submitBtn").click()

        assert "singin page" in self.driver.title
        assert "wrong password. try again" in self.driver.page_source

        self.driver.find_element_by_id("signinUser").send_keys(self.new_user.userName)
        self.driver.find_element_by_id("signinPassword").send_keys("1234567")
        self.driver.find_element_by_id("submitBtn").click()

        assert "user panel" in self.driver.title


    def tearDown(self):
        self.driver.close()
        self.assertTrue(True)

