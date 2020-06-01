import unittest
from billbook_v1 import Login_Test,Manager_Add_Test

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Login_Test.Login('test_login_success'))
    #suite.addTest(Login_Test.Login('test_login_with_wrong_user'))
    suite.addTest(Manager_Add_Test.AddManager('test_createManager'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())