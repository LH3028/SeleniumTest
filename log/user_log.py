# -*- coding:utf-8 -*-
__author__ = "longhao"
__date__ = "2021.4.7"

import logging
import os
from datetime import datetime

class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()  #创建logger对象
        self.logger.setLevel(logging.DEBUG)  #设置logger对象的日志等级
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir, "logs")
        #print(log_dir)
        log_file = datetime.now().strftime("%Y-%m-%d") + ".log"
        log_filepath = log_dir + "\\" + log_file

        self.file_handle = logging.FileHandler(log_filepath)  # 日志输入文件
        #self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s %(filename)s ----> %(funcName)s:%(levelno)s ----> %(levelname)s:%(message)s")
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)



    def get_log(self):
        return self.logger

    def close_handle(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)  #删除handle流

if __name__=="__main__":
    user_log = UserLog()
    log = user_log.get_log()
    log.debug("test 111111111111")
    user_log.close_handle()