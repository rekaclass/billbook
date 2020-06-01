import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest
from billbook_v1 import LoginUtil

class ViewManager(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\projects\learning\drivers\chromedriver.exe")
        self.driver.get("http://billbooks.co.in/demo/bills/index.php")

    def test_ViewManager(self, element=None):
        LoginUtil.login(self.driver, 'admin', 'admin')
        self.driver.find_element_by_id("navbarDropdownMenuLink").click()
        self.driver.find_element_by_link_text("recent_actors View Manager").click()
        assert 'View Employees' in self.driver.title
        assert "aa11" in self.driver.find_element_by_tag_name("body").text
        #assert element.text == 'Ramki'
        self.driver.find_element_by_xpath("//*[@id='example']/tbody/tr[1]/td[7]/a[1]").click()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()

