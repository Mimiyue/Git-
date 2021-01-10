from selenium import webdriver
import unittest

class jenkinsTest(unittest.TestCase):
    def test01(self):
        print("hello Git")
    def test02(self):
        print("hello Git1")
        print("hello Git2")
        print("hello Git3")
    def test03(self):
        print("hello Git4")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    cases = loader.loadTestsFromTestCase(jenkinsTest)
    suite.addTests(cases)
    runner = unittest.TextTestRunner(stream=open('res.txt', 'a'), verbosity=2)
    runner.run(suite)

