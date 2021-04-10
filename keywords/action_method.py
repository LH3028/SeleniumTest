# -*- coding:utf-8 -*-
__author__ = "longhao"
__date__ = "2021.4.6"

from selenium import webdriver
from base.find_element import FindElement
import time


class ActionMethod(object):
    def open_browser(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()

        else:
            self.driver = webdriver.Firefox()

    def get_url(self, url):

        self.driver.get(url)

    def get_element(self, key):
        "获取元素"
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    def send_value(self, key, value):
        self.get_element(key).send_keys(value)

    def click_element(self, key):
        self.get_element(key).click()

    def sleep_time(self, s):
        time.sleep(s)

    def close_browser(self):
        self.driver.close()

    def get_title(self):
        return self.driver.title
