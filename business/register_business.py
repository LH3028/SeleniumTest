# -*- coding:utf-8 -*-
__author__ = "longhao"
__date__ = "2021.3.15"

from handle.register_handle import RegisterHandle
class RegisterBusiness(object):
    def __init__(self, driver):
        self.reg_handle = RegisterHandle(driver)

    def user_common(self, email, name, password, filename):
        self.reg_handle.send_user_email(email)
        self.reg_handle.send_user_name(name)
        self.reg_handle.send_user_password(password)
        self.reg_handle.send_user_captcha(filename)
        self.reg_handle.click_register()

    def register_email_error(self, email, name, password, filename):
        """执行注册操作"""
        self.user_common(email, name, password, filename)
        if self.reg_handle.get_error_msg("email_error", "请输入有效的电子邮箱地址") == None:
            print("注册邮箱检验失败")
            return True
        else:
            return False

    def register_func(self,email,username,password,captcha,error_element,error_msg):
        self.user_common(email, username, password, captcha)
        if self.reg_handle.get_error_msg(error_element,error_msg) == None:
            print("注册邮箱检验不成功")
            return True
        else:
            return False

    def register_username_error(self, email, name, password, filename):
        self.user_common(email, name, password, filename)
        if self.reg_handle.get_error_msg("username_error_error", "字符长度必须大于等于4，一个中文算两个字符") == None:
            print("注册用户名检验失败")
            return True
        else:
            return False

    def register_password_error(self, email, name, password, filename):
        self.user_common(email, name, password, filename)
        if self.reg_handle.get_error_msg("password_error", "最少输入5个字符") == None:
            print("注册密码检验失败")
            return True
        else:
            return False

    def register_captcha_error(self, email, name, password, filename):
        self.user_common(email, name, password, filename)
        if self.reg_handle.get_error_msg("captcha_error", "验证码错误") == None:
            print("注册验证码检验失败")
            return True
        else:
            return False

    def register_success(self):
        if self.reg_handle.click_register_button_text():
            return True
        else:
            return False
