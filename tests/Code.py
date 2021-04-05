import json
import urllib
import urllib.request
import base64
import re
def code(img):
    host = 'https://codevirify.market.alicloudapi.com'
    path = '/icredit_ai_image/verify_code/v1'
    #阿里云APPCODE
    appcode = 'fca475f84b8942c09c62b389d2df8e0d'
    url = host + path
    bodys = {}
    querys = ""
    f = open(img, 'rb')
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
       return content.decode('utf-8')
add='D:\Python\HtmlTestRunner\Htmltestrunner\Png\getcode_1.png'
print(code(add))
print(json.loads(code(add))["VERIFY_CODE_ENTITY"]['VERIFY_CODE'])

