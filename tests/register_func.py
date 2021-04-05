from selenium import webdriver
from PIL import Image
import time , random , json
import urllib
import urllib.request
import base64
from base.find_element import FindElement
class RegisterFunc(object):
    def __init__(self,url):
        self.driver = self.get_driver(url)

    def get_driver(self,url):
        "获取driver"
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    def send_user_info(self,key,data):
        """发送用户注册信息"""

        self.get_user_element(key).send_keys(data)

    def get_user_element(self,key):
        """获取用户元素"""

        fe = FindElement(self.driver)
        user_element = fe.get_element(key)
        return user_element

    def get_range_user(self):
        """获取随机用户名"""
        str = "1234567890abcdefghijklmnopqlstuvwxzy"
        user_info = ''.join(random.sample(str, 8))
        return user_info

    def get_range_email(self):
        """获取随机邮箱"""

        email = ''
        user_info = self.get_range_user()
        print(type(user_info))
        if not user_info[0:1].isdigit():
            email = ''.join(user_info) + "@163.com"

        else:
            user_info = random.choice("abcdefghijklmnopqrrstuvwxyz") + user_info[1:0]
            email = ''.join(user_info) + "@163.com"
        return email

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

    def main(self):

        file_name = "D:\Python\HtmlTestRunner\Htmltestrunner\Png\getcode_1.png"
        user_email = self.get_range_email()
        user_name = self.get_range_user()
        self.get_image(file_name)
        captcha_code = self.get_image_code(file_name)
        self.send_user_info('user_email', user_email)
        self.send_user_info('user_name', user_name)
        self.send_user_info('password', "123456")
        self.send_user_info("captcha_code", captcha_code)
        self.get_user_element('register_button').click()
        code_error = self.get_user_element("captcha_code_error")
        if code_error is None:
            print("注册成功")
        else:
            print("注册失败")
            self.driver.save_screenshot("D:\Python\HtmlTestRunner\Htmltestrunner\Png\code_error.png")
        time.sleep(10)
        self.driver.close()

if __name__ == '__main__':
    RegisterFunc("http://www.5itest.cn/register").main()
