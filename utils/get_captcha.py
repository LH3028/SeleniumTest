# -*- coding:utf-8 -*-
__author__ = "longhao"
__date__ = "2021.3.20"

from PIL import Image
import time, json
import urllib.parse
import urllib.request
import base64

class GetCaptcha(object):
    def __init__(self, driver):
        self.driver = driver


    def get_image(self,file_name):

        """获取验证码图片"""
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id("getcode_num")
        x = code_element.location["x"]
        y = code_element.location["y"]
        width = code_element.size["width"] + x
        height = code_element.size["height"] + y
        im = Image.open(file_name)
        img = im.crop((x, y, width, height))
        img.save(file_name)

    def get_image_code(self,file_name):
        """调用接口识别图片验证码"""

        host = 'https://codevirify.market.alicloudapi.com'
        path = '/icredit_ai_image/verify_code/v1'
        # 阿里云APPCODE
        appcode = 'fca475f84b8942c09c62b389d2df8e0d'
        url = host + path
        bodys = {}
        querys = ""
        f = open(file_name, 'rb')
        contents = base64.b64encode(f.read())
        f.close()
        bodys['IMAGE'] = contents
        bodys['IMAGE_TYPE'] = '0'
        post_data = urllib.parse.urlencode(bodys).encode('utf-8')
        request = urllib.request.Request(url, post_data)
        request.add_header('Authorization', 'APPCODE ' + appcode)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
        response = urllib.request.urlopen(request)
        content = response.read()
        if (content):
            return json.loads(content.decode('utf-8'))["VERIFY_CODE_ENTITY"]['VERIFY_CODE']