from selenium import webdriver
import unittest
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
import Utils


class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.url = "http://localhost/Mainpage.htm"
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

        self.new_user = user

    def test_see_account_info(self):
        self.driver.find_element_by_id("accountBtn").click()
        assert "account information" in self.driver.title #correct page
        assert self.driver.find_element_by_id("name") is self.new_user.userName
        assert self.driver.find_element_by_id("email") is self.new_user.e_mail
        assert self.driver.find_element_by_id("bankaccount") is self.new_user.bankAccount
        assert self.driver.find_element_by_id("phone") is self.new_user.phone
        assert self.driver.find_element_by_id("notif") is "email"


    def tearDown(self):
        self.driver.close()
        self.assertTrue(True)


    # def signup_user(self, user):
