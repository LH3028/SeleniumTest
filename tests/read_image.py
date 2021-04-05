# from PIL import Image
# import pytesseract
# image = Image.open("D:\Python\毕设\Htmltestrunner\Png\getcode_1.png")
# code = pytesseract.image_to_string(image)
# print(code)

import requests
from PIL import Image
import pytesseract
def main():
    img = Image.open('D:\Python\HtmlTestRunner\Htmltestrunner\Png\getcode_1.png')
    result = pytesseract.image_to_string(img)
    print("未进行处理，出错机率很大:", result)
    img = img.convert('L')  # 进行灰度处理
    threshold = 128  # 二值化阈值
    t_list = []
    for i in range(256):
        if i < threshold:
            t_list.append(0)
        else:
            t_list.append(1)
    img = img.point(t_list, '1')

    img.show()
    result = pytesseract.image_to_string(img)
    print("处理后：", result)


if __name__ == '__main__':
    main()