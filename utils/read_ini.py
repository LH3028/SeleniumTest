# -*- coding: utf-8 -*-
__author__="HaoLong"
__data__="2021/1/10"

import configparser


class ReadIni(object):
    def __init__(self,filename=None,node=None):
        if filename == None:
            self.filename = "D:\Python\HtmlTestRunner\Htmltestrunner\config\LocalElement.ini"
        if node == None:
            self.node ="RegisterElement"
        else:
            self.node = node
        self.cf = self.load_ini(self.filename)

    def load_ini(self,filename):
        cf = configparser.ConfigParser()
        cf.read(filename)
        return cf

    def get_value(self,key):
        data = self.cf.get(self.node, key)
        return data



if __name__ == "__main__":
    print(ReadIni().get_value("user_name"))
