from selenium import webdriver
import unittest
from PIL import Image
from HTMLTestRunner_cn import HTMLTestRunner
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from tests.Base64 import Base64
import urllib
import urllib.request
import base64
import re
import time
driver = webdriver.Firefox()
driver.get("http://www.5itest.cn/register")
time.sleep(5)
res= ec.title_contains("注册")
print(res)
email_element = driver.find_element_by_id("register_email")
driver.save_screenshot("D:\Python\Htmltestrunner\Htmltestrunner\Png\getcode.png")
code_element = driver.find_element_by_id("getcode_num")
print(code_element.location)   #获取验证码页面坐标
x = code_element.location["x"]
y = code_element.location["y"]
width = code_element.size["width"]+x
height = code_element.size["height"]+y
driver.close()
im = Image.open("D:\Python\HtmlTestRunner\Htmltestrunner\Png\getcode.png")
img = im.crop((x,y,width,height))
img.save("D:\Python\Htmltestrunner\Htmltestrunner\Png\getcode_1.png")
image='D:\Python\HtmlTestRunner\Htmltestrunner\Png\getcode_1.png'
host = 'https://codevirify.market.alicloudapi.com'
path = '/icredit_ai_image/verify_code/v1'
#阿里云APPCODE
appcode = 'fca475f84b8942c09c62b389d2df8e0d'
url = host + path
bodys = {}
querys = ""
f = open(image, 'rb')
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
   print(content.decode('utf-8'))


