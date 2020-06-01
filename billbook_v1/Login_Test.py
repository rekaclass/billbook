import unittest
from selenium import webdriver
from billbook_v1 import LoginUtil
#from pyunitreport import HTMLTestRunner

user_succ='admin'
pass_succ='admin'
pass_wrong='test'
user_wrong='test'

class Login(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="C:\projects\learning\drivers\chromedriver.exe")

    def test_login_success(self):
        driver = self.driver
        driver.get("http://billbooks.co.in/demo/bills/index.php")
        LoginUtil.login(driver, user_succ, pass_succ)
        assert driver.title == 'BILL BOOKS'

    def test_login_with_wrong_user(self):
        driver = self.driver
        driver.get("http://billbooks.co.in/demo/bills/index.php")
        LoginUtil.login(driver, user_wrong, pass_succ)
        assert driver.title == 'Bill Books: Login'

    def test_login_with_wrong_pass(self):
        driver = self.driver
        driver.get("http://billbooks.co.in/demo/bills/index.php")
        LoginUtil.login(driver, user_succ, pass_wrong)
        assert driver.title == 'Bill Books: Login'

   # @unittest.skip("demonstrating skipping")
    def test_login_with_wrong_user_pass(self):
        driver = self.driver
        driver.get("http://billbooks.co.in/demo/bills/index.php")
        LoginUtil.login(driver, user_wrong, pass_wrong)
        assert driver.title == 'Bill Books: Login'

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=HTMLTestRunner(output='c:\projects\learning\testselenium\report'))