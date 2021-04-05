from selenium import webdriver
import unittest
from TestRunner.HTMLTestRunner import HTMLTestRunner
import time

class Baidu(unittest.TestCase):
    def setUp(self):
        '''测试准备工作'''
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = 'https://www.baidu.com/'

    def test_baidu_search(self):
        '''测试百度搜索'''
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').clear()
        self.driver.find_element_by_id('kw').send_keys('测试工程师')
        self.driver.find_element_by_id('su').click()

    def tearDown(self):
        '''资源释放'''
        self.driver.quit()

if __name__ == '__main__':
    testunit = unittest.TestSuite()                    #初始化测试用例集合对象，构建测试套件
    testunit.addTest(Baidu("test_baidu_search"))       #把测试用例加入到测试用例集合中去，将用例加入到检测套件中
    fp = open('D://Python/HtmlTestRunner/Htmltestrunner/reports/result.html','wb')#定义测试报告存放路径
    runner = HTMLTestRunner(stream=fp,title='百度搜索测试报告',description='用例执行情况')#定义测试报告
    runner.run(testunit)#执行测试用例
    fp.close() 