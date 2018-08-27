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


class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.url = "http://localhost/test.html"
        self.driver.get(self.url)


    def test_1(self):
        pass

    def tearDown(self):
        self.driver.close()
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()