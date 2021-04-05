# -*- coding:utf-8 -*-
__author__ = "longhao"
__date__ = "2021.3.15"

from base.find_element import FindElement


class RegisterPage(object):

    def __init__(self, driver):
        self.find_ele = FindElement(driver)

    def get_email_element(self):
        return self.find_ele.get_element("user_email")

    def get_username_element(self):
        return self.find_ele.get_element("user_name")

    def get_password_element(self):
        return self.find_ele.get_element("password")

    def get_captcha_element(self):
        return self.find_ele.get_element("captcha_code")

    def get_register_button_element(self):
        return self.find_ele.get_element("register_button")

    def get_user_email_error_element(self):
        return self.find_ele.get_element("user_email_error")

    def get_user_name_error_element(self):
        return self.find_ele.get_element("user_name_error")

    def get_password_error_element(self):
        return self.find_ele.get_element("password_error")

    def get_captcha_code_error_element(self):
        return self.find_ele.get_element("captcha_code_error")

