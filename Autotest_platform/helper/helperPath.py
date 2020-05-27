#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 10:32
# @Author  : lixiaofeng
# @Site    : 
# @File    : settings.py
# @Software: PyCharm


from django.conf import settings
from django.contrib.auth.models import User
import os, platform, time, re, logging, shutil

pattern = '/' if platform.system() != 'Windows' else '\\'
log = logging.getLogger('log')  # 初始化log


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


def register_info_logic(username, password, pswd_again, email):
    """
    注册新用户逻辑
    :param username:
    :param password:
    :param pswd_again:
    :param email:
    :return:
    """
    if email:
        if not re.match('.+@.+\..+$', email):
            return "邮箱格式错误！"
    if username == '' or password == '' or pswd_again == '':
        return "用户名、密码不能为空！"
    elif len(username) > 50 or len(password) > 50 or len(email) > 50:
        return "用户名、密码及邮箱必须小于50位!"
    elif 6 > len(username) or 6 > len(password):
        return "用户名、密码必须大于6位!"
    elif password != pswd_again:
        return "两次密码输入不一致！"
    else:
        try:
            User.objects.get(username=username)
            return "用户名已经存在！"
        except User.DoesNotExist:
            return 'ok'


def change_info_logic(new_password):
    """
    修改密码逻辑
    :param new_password:
    :return:
    """
    if not new_password:
        return "'字段不能为空！'"
    elif len(new_password) < 6:
        return '输入字段长度不够！<新密码必须大于6位.>'
    elif len(new_password) > 50:
        return '输入字段过长！<新密码必须小于50位.>'
    else:
        return 'ok'


def get_file_sorted(file_path):
    """最后修改时间顺序升序排列 os.path.getmtime()->获取文件最后修改时间"""
    dir_list = os.listdir(file_path)
    if not dir_list:
        return False
    else:
        dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
        return dir_list


def delete_testcase(file_path):
    """
    清理产生的测试文件和报告
    :param file_path:
    :return:
    """
    if os.path.exists(file_path):
        dir_list = get_file_sorted(file_path)
        if dir_list and len(dir_list) > 10:
            dir_list = dir_list[0:-10]
            for d in dir_list:
                d_path = os.path.join(file_path, d)
                if os.path.isdir(d_path):
                    try:
                        shutil.rmtree(d_path)
                    except PermissionError as e:
                        log.error('权限错误，删除日志文件失败！{}'.format(d_path))
                elif os.path.isfile(d_path):
                    try:
                        os.remove(d_path)
                    except PermissionError as e:
                        log.error('权限错误，删除日志文件失败！{}'.format(d_path))
    else:
        log.error("要删除的目录不存在！")
