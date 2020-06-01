import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest
from billbook_v1 import LoginUtil


class AddManager(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\projects\learning\drivers\chromedriver.exe")
        self.driver.get("http://billbooks.co.in/demo/bills/index.php")

    def test_createManager(self):
        LoginUtil.login(self.driver, 'admin', 'admin')
        self.driver.find_element_by_id("navbarDropdownMenuLink").click()
        self.driver.find_element_by_link_text("group_add Add New Manager").click()
        self.assertEqual( self.driver.title,'BILL BOOKS: Create Staff')
        time.sleep(2)
        self.driver.find_element_by_id("username").send_keys("reka")
        self.driver.find_element_by_id("password").send_keys("password")
        self.driver.find_element_by_id("name").send_keys("Reka")
        self.driver.find_element_by_id("email").send_keys("reka@gmail.com")
        contact = self.driver.find_element_by_id("contno")
        contact.send_keys("7205199631")

        roll = self.driver.find_element_by_id("role_id")
        select = Select(self.driver.find_element_by_id("role_id"))
        select.select_by_value("1")
        time.sleep(3)
        # gender = driver.find_element_by_value("Female").click()
        submit = self.driver.find_element_by_name("submit").click()
        #print(self.driver.title)
        assert 'View Employees' in self.driver.title
        time.sleep(5)


    #def tearDown(self):
    #   self.driver.quit()
if __name__ == '__main__':
    unittest.main()


