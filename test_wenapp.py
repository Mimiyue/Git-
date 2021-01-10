from selenium import webdriver
import unittest
import pytest
# class jenkinsTest(unittest.TestCase):
print("start testing")
def test_01():
    print("hello Git")
def test_02():
    print("hello Git1")
    print("hello Git2")
    print("hello Git3")
def test_03():
    print("hello Git4")

import pytest
pytest.main(['wenapp.py','-vv','--alluredir=./allure-results'])


# if __name__ == '__main__':
#     unittest.main(['wenapp.py','-vv','--alluredir=./allure-results'])
    # suite = unittest.TestSuite()
    # loader = unittest.TestLoader()
    # cases = loader.loadTestsFromTestCase(jenkinsTest)
    # suite.addTests(cases)
    # runner = unittest.TextTestRunner(stream=open('res.txt', 'a'), verbosity=2)
    # runner.run(suite)

