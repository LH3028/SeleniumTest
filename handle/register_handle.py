# -*- coding:utf-8 -*-
__author__ = "longhao"
__date__ = "2021.3.15"

from page.register_page import RegisterPage
from utils.get_captcha import GetCaptcha


class RegisterHandle(object):

    def __init__(self, driver):
        self.driver = driver
        self.reg_page = RegisterPage(driver)

    def send_user_email(self, email):
        """输入邮箱地址"""
        self.reg_page.get_email_element().send_keys(email)

    def send_user_name(self, name):
        """输入用户名"""
        self.reg_page.get_username_element().send_keys(name)

    def send_user_password(self, password):
        """输入密码"""
        self.reg_page.get_password_element().send_keys(password)

    def send_user_captcha(self, filename):
        """输入验证码"""

        #captcha_code = GetCaptcha(self.driver)
        #captcha_code.get_image(filename)
        #code = captcha_code.get_image_code(filename)
        self.reg_page.get_captcha_element().send_keys(filename)


    def get_error_msg(self, info, error_msg):
        """获取错误信息"""
        try:
            if info == "user_email_error":
                text = self.reg_page.get_user_email_error_element().text

            elif info == "user_name_error":
                text = self.reg_page.get_user_name_error_element().text

            elif info == "password_error":
                text = self.reg_page.get_password_error_element().text

            else:
                text = self.reg_page.get_captcha_code_error_element().text
        except:
            text = None
        return text

    def click_register(self):
        """点击注册"""
        self.reg_page.get_register_button_element().click()

    def click_register_button_text(self):
        try:
            text = self.reg_page.get_register_button_element().text
        except Exception as e:
            text = None
        return text