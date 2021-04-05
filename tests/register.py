from selenium import webdriver
from PIL import Image
import time , random , json
import urllib
import urllib.request
import base64
import json

driver = webdriver.Firefox()
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()  #浏览器窗口最大化
    time.sleep(5)

def get_element(id):
    element = driver.find_element_by_id(id)
    return element

def get_range_user():
    str = "1234567890abcdefghijklmnopqlstuvwxzy"
    user_info = ''.join(random.sample(str,8))
    return user_info

def get_range_email():

    email = ''
    user_info = get_range_user()
    print(type(user_info))
    if not user_info[0:1].isdigit():
        email = ''.join(user_info)+"@163.com"

    else:
        user_info = random.choice("abcdefghijklmnopqrrstuvwxyz")+user_info[1:0]
        email = ''.join(user_info) + "@163.com"
    return email

def get_image(file_name):

    "获取验证码图片"
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id("getcode_num")
    x = code_element.location["x"]
    y = code_element.location["y"]
    width = code_element.size["width"] + x
    height = code_element.size["height"] + y
    im = Image.open(file_name)
    img = im.crop((x, y, width, height))
    img.save(file_name)

def get_image_code(file_name):
    "调用接口识别图片验证码"

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

def run_main():

    file_name = "D:\Python\HtmlTestRunner\Htmltestrunner\Png\getcode_1.png"
    user_email = get_range_email()
    user_name = get_range_user()
    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name)
    get_element("register_password").send_keys("123456")
    get_image(file_name)
    text=get_image_code(file_name)

    get_element("captcha_code").send_keys(text)
    get_element("register-btn").click()


if __name__ == '__main__':
    run_main()
