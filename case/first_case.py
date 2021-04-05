# -*- coding:utf-8 -*-
__author__ = "longhao"
__date__ = "2021.3.15"

from notebook.jstest import report

from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import warnings
from TestRunner.HTMLTestRunner import HTMLTestRunner
from TestRunner import SMTP
from time import sleep
import time
import os, sys


class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dir = os.path.dirname(os.getcwd())
        cls.filename = os.path.join(dir, "Png")+"/test.png"

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        sleep(3)
        #self.driver.maximize_window()
        self.reg_business = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(1)
        for method_name, error in self._outcome.errors:
            if error:
                dir = os.path.dirname(os.getcwd())
                images_dir = os.path.join(dir, "Png")
                case_name = self._testMethodName
                self.driver.save_screenshot(images_dir+"/%s.png" % case_name)
                print("截图成功")
        self.driver.close()


    def test_register_email_error(self):
        email_error = self.reg_business.register_email_error("xxx", "longhao", "123456", self.filename)
        #self.assertFalse(email_error, "注册失败，此条用例执行成功")
        if email_error:
            print("注册成功，此条用例执行失败")
        else:
            print("注册失败，此条用例执行成功")


    def test_register_username_error(self):
        username_error = self.reg_business.register_username_error("272902959@qq.com", "long", "123456", self.filename)
        #self.assertFalse(username_error, "注册失败，此条用例执行成功")
        if username_error:
            print("注册成功，此条用例执行失败")
        else:
            print("注册失败，此条用例执行成功")

    def test_register_password_error(self):
        password_error = self.reg_business.register_password_error("272902959@qq.com", "longhao", "123",self.filename)
        #self.assertFalse(password_error, "注册失败，此条用例执行成功")
        if password_error:
            print("注册成功，此条用例执行失败")
        else:
            print("注册失败，此条用例执行成功")

    def test_register_captcha_error(self):
        captcha_error = self.reg_business.register_captcha_error("xxx", "longhao", "123456", self.filename)
        #self.assertFalse(captcha_error, "注册失败，此条用例执行成功")
        if captcha_error:
            print("注册成功，此条用例执行成功")
        else:
            print("注册失败，此条用例执行成功")
    def test_register_success(self):
        self.reg_business.user_common("272902959@qq.com", "longhao", "123456", self.filename)
        if self.reg_business.register_success():
            print("注册失败")
        else:
            print("注册成功")


'''
def main():
    fc = FirstCase()
    fc.test_register_email_error()
    fc.test_register_username_error()
    fc.test_register_password_error()
    fc.test_register_captcha_error()
    fc.test_register_success()
'''

if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(FirstCase("test_register_email_error"))
    suit.addTest(FirstCase("test_register_username_error"))
    suit.addTest(FirstCase("test_register_password_error"))
    suit.addTest(FirstCase("test_register_captcha_error"))
    suit.addTest(FirstCase("test_register_success"))
    fp = open('D://Python/HtmlTestRunner/Htmltestrunner/reports/first_case.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title='第一次测试报告', description='用例执行情况', verbosity=2)
    runner.run(suit)  # 执行测试用例
    smtp = SMTP(user="24911068887@qq.com", password="LH4830328051716", host="mail.qq.com")
    smtp.sender(to="2729029598@qq.com", attachments = report)
    fp.close()
