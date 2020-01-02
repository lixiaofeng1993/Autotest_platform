#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 10:32
# @Author  : lixiaofeng
# @Site    : 
# @File    : settings.py
# @Software: PyCharm


from django.conf import settings
import os, platform, time

pattern = '/' if platform.system() != 'Windows' else '\\'


class CustomException(Exception):
    """自定义异常类"""

    def __init__(self, error):
        self.error = error

    def __str__(self):
        exception_msg = "Message: %s\n" % self.error
        return exception_msg


class NoTextFountException(CustomException):
    """
    没有发现文本异常
    """
    pass


def check_dir(path):
    """
    检查目录是否存在，不存在则创建目录
    :param path:
    :return: path
    """
    if not os.path.exists(path):
        os.mkdir(path)
    return path


def check_file(path):
    """
    检查文件是否存在，不存在则抛出错误
    :param path:
    :return:
    """
    if not os.path.exists(path):
        return False
    else:
        return path


BASE_DIR = settings.BASE_DIR

driver_path = check_dir(os.path.join(BASE_DIR, "driver"))  # 驱动文件路径

log_path = check_dir(os.path.join(BASE_DIR, "logs"))  # 日志路径

hour = time.strftime('%Y-%m-%d')
now = time.strftime('%Y-%m-%d %H-%M-%S')
