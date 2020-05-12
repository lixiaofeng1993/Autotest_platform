#!/user/bin/env python
# coding=utf-8
'''
# 创 建 人: 李先生
# 文 件 名: public.py
# 说   明: 
# 创建时间: 2020/5/2 14:20
'''

import time, platform, os, logging
import matplotlib as mpl
from django.conf import settings
from matplotlib import pyplot as plt
# from matplotlib.font_manager import FontProperties
from datetime import datetime
from collections import OrderedDict

log = logging.getLogger('log')  # 初始化log


def DrawPie(pass_num=0, error=0, skip=0):
    """
    绘制饼图用pie
    :return:
    """
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    now_time = int(time.mktime(time.strptime(start_time, '%Y-%m-%d %H:%M:%S')))
    mpl.rcParams[u'font.sans-serif'] = ['simhei']
    mpl.rcParams['axes.unicode_minus'] = False
    # 调节图形大小，宽，高
    # plt.figure(figsize=(6, 9))
    # 定义饼状图的标签，标签是列表
    labels = 'pass', 'error', "skip"
    # 每个标签占多大，会自动去算百分比
    my_labels = [pass_num, error, skip]
    colors = ['green', 'red', "grey"]
    # 将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
    explode = (0.05, 0, 0)

    patches, l_text, p_text = plt.pie(my_labels, explode=explode, labels=labels, colors=colors,
                                      labeldistance=1.1, autopct='%3.1f%%', shadow=False,
                                      startangle=90, pctdistance=0.6, textprops={'fontsize': 12, 'color': 'w'})

    # labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
    # autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    # shadow，饼是否有阴影
    # startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    # pctdistance，百分比的text离圆心的距离
    # patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

    # 改变文本的大小
    # 方法是把每一个text遍历。调用set_size方法设置它的属性
    for t in l_text:
        t.set_size = (30)
    for t in p_text:
        t.set_size = (20)
    plt.title('Running results of test cases')
    # 显示图例,去掉重复的标签
    colors, labels = plt.gca().get_legend_handles_labels()
    by_labels = OrderedDict(zip(labels, colors))
    plt.legend(by_labels.values(), by_labels.keys(), loc='upper left')
    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    # plt.show()
    # 保存饼图
    if platform.system() == "Windows":
        pic_path = settings.MEDIA_ROOT
    else:
        pic_path = '/www/wwwroot/server/EasyTest/media'
    imgPath = os.path.join(pic_path, str(now_time) + "pie.png")
    plt.savefig(imgPath)
    plt.tight_layout()
    plt.cla()  # 不覆盖
    pie_name = str(now_time) + "pie.png"
    return pie_name


def remove_logs(path):
    """
    到期删除日志文件
    :param path:
    :return:
    """
    if os.path.isdir(path):
        file_list = os.listdir(path)  # 返回目录下的文件list
        now_time = datetime.now()
        num = 0
        for file in file_list:
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                file_ctime = datetime(*time.localtime(os.path.getctime(file_path))[:6])
                if (now_time - file_ctime).days > 6:
                    try:
                        os.remove(file_path)
                        num += 1
                        log.info('------删除文件------->>> {}'.format(file_path))
                    except PermissionError as e:
                        log.warning('删除文件失败：{}'.format(e))
                        # if name not in file_path and "pie" in file_path:
                        #     try:
                        #         os.remove(file_path)
                        #         num += 1
                        #         log.info('------删除文件------->>> {}'.format(file_path))
                        #     except PermissionError as e:
                        #         log.warning('删除文件失败：{}'.format(e))
            else:
                log.info('文件夹跳过：{}'.format(file_path))
        return num
    else:
        pic_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.isfile(pic_path):
            try:
                os.remove(pic_path)
                log.info('------删除文件------->>> {}'.format(pic_path))
            except PermissionError as e:
                log.warning('删除文件失败：{}'.format(e))
        else:
            log.warning('不是文件或者文件不存在：{}'.format(pic_path))
