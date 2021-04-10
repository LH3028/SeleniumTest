# -*- coding:utf-8 -*-
__author__ = "longhao"
__date__ = "2021.3.25"

from selenium import webdriver
import unittest
import warnings
from TestRunner.HTMLTestRunner import HTMLTestRunner
from time import sleep
import time
import os
import ddt
from business.register_business import RegisterBusiness
from utils.op_excel import OpExcel

data = OpExcel().get_data


@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dirpath = os.path.dirname(os.getcwd())
        cls.filename = os.path.join(dirpath, "Png") + "/test.png"

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        sleep(3)
        # self.driver.maximize_window()
        self.reg_business = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(1)
        for method_name, error in self._outcome.errors:
            if error:
                dir = os.path.dirname(os.getcwd())
                images_dir = os.path.join(dir, "Png")
                case_name = self._testMethodName
                self.driver.save_screenshot(images_dir + "/%s.png" % case_name)
        self.driver.close()
        print("*" * 25 + "分割线" + "*" * 25)

    """
    @ddt.data(
        ["12a", "longhao", "123456", "captcha", "user_email_error", "请输入有效的电子邮件地址"],
        ["qq.com", "longhao1", "123456", "captcha", "user_email_error", "请输入有效的电子邮件地址"],
        ["1221312@qq.com", "longhao2", "123456", "captcha", "user_email_error", "请输入有效的电子邮件地址"],
        ["1221312@qq.com", "lon", "123456", "captcha", "user_name_error", "字符长度必须大于等于4，一个中文算两个字符"],
        ["1221312@qq.com", "1234", "123456", "captcha", "user_name_error", "字符长度必须大于等于4，一个中文算两个字符"],
        ["1221312@qq.com", "longhao2", "123456", "captcha", "user_name_error", "字符长度必须大于等于4，一个中文算两个字符"],
        ["1221312@qq.com", "longhao2", "123", "captcha", "password_error", "最少输入5个字符"],
        ["1221312@qq.com", "longhao2", "1234", "captcha", "password_error", "最少输入5个字符"],
        ["1221312@qq.com", "longhao2", "123456", "captcha", "password_error", "最少输入5个字符"]
    )
    @ddt.unpack
    """

    @ddt.data(*data)
    def test_register_case(self, data):
        print(data)
        email, username, password, captcha, error_element, error_msg = data
        email_error = self.reg_business.register_func(email, username, password, captcha, error_element, error_msg)
        self.assertFalse(email_error, "测试失败")


if __name__ == "__main__":
    suit = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    fp = open('D://Python/HtmlTestRunner/Htmltestrunner/reports/firstddt01_case.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title='第一次测试报告', description='用例执行情况', verbosity=2)
    runner.run(suit)  # 执行测试用例
    fp.close()

    """dir = os.path.dirname(os.getcwd())
    report_dir = os.path.join(dir, "reports")
    file_path = report_dir + "/first_ddt_case.html"
    fp = open(file_path, "wb")
    suite = unittest.TextSuite()
    suite.addTest(FirstDdtCase("test_register_case"))
    runner = HTMLTestRunner(stream=fp, title='第一次测试报告', description='用例执行情况', verbosity=2)
    runner.run(suite)  # 执行测试用例
    """
