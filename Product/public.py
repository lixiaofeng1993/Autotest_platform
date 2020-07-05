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
from django.http import HttpResponseRedirect
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


def check_team(fn):
    from .models import TeamUsers

    def wrapper(request, *args, **kwargs):
        user_id = request.session.get('user_id', None)
        tid = request.session.get('tid', None)
        if not tid:
            return HttpResponseRedirect('/team/')
        status = 0
        tus = TeamUsers.objects.filter(team_id=tid).filter(user_id=user_id)
        if tus:
            for t in tus:
                status = t.status
        if status == 0:
            return HttpResponseRedirect('/team/')
        else:
            return fn(request, *args, **kwargs)

    return wrapper


def model_nav(request):
    from .models import ModularTable
    from Autotest_platform.helper.util import get_model

    tid = request.session.get('tid', None)
    model_list = get_model(ModularTable, get=False, team_id=tid)
    return tid, model_list


def create_model(tid):
    from .models import ModularTable
    from Autotest_platform.helper.util import get_model
    mt_list = []
    sign_dict = [
        {"id": 1, "model_name": "项目管理", "url": "/admin/project", 'Icon': 'fa fa-desktop', 'team_id': tid},
        {"id": 2, "model_name": "页面管理", "url": "/admin/page", 'Icon': 'fa fa-bar-chart', 'team_id': tid},
        {"id": 3, "model_name": "页面元素", "url": "/admin/element", 'Icon': 'fa fa-fw fa-qrcode', 'team_id': tid},
        {"id": 4, "model_name": "关键字库", "url": "/admin/keyword", 'Icon': 'fa fa-fw fa-table', 'team_id': tid},
        {"id": 5, "model_name": "测试用例", "url": "/admin/testcase", 'Icon': 'fa fa-w fa-edit', 'team_id': tid},
        {"id": 6, "model_name": "测试结果", "url": "/admin/result", 'Icon': 'fa fa-fw fa-file', 'team_id': tid},
        {"id": 7, "model_name": "登录配置", "url": "/admin/loginConfig", 'Icon': 'fa fa-fw fa-building',
         'team_id': tid},
        {"id": 8, "model_name": "任务管理", "url": "/admin/task", 'Icon': 'fa fa-fw fa-sitemap', 'team_id': tid},
    ]
    for signer in sign_dict:
        mt_list.append(
            ModularTable(order_id=signer["id"], model_name=signer["model_name"], url=signer["url"], Icon=signer["Icon"],
                         team_id=signer["team_id"]))
    ModularTable.objects.bulk_create(mt_list)
    mt = get_model(ModularTable, get=False, team_id=tid)
    return mt
