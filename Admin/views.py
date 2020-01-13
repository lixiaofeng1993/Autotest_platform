# coding:utf-8
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from Autotest_platform.helper.helperPath import register_info_logic
import logging

log = logging.getLogger('log')  # 初始化log


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)  # 认证给出的用户名和密码
        if user is not None and user.is_active:  # 判断用户名和密码是否有效
            auth.login(request, user)
            request.session['user'] = username  # 跨请求的保持user参数
            response = HttpResponseRedirect('/admin/index')
            return response
        else:
            messages.add_message(request, messages.WARNING, '账户或者密码错误，请检查')
            return render(request, 'page/1登录.html')
    elif request.method == "GET":
        return render(request, 'page/1登录.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'page/register.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        pswd_again = request.POST.get('pswd-again', '')
        email = request.POST.get('email', '')
        msg = register_info_logic(username, password, pswd_again, email)
        if msg != 'ok':
            log.error('register error：{}'.format(msg))
            return render(request, 'page/register.html', {'error': msg})
        else:
            User.objects.create_user(username=username, password=password, email=email)
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                request.session['user'] = username  # 将session信息记录到浏览器
                user_ = User.objects.get(username=username)
                request.session['user_id'] = user_.id  # 将session信息记录到浏览器
                response = HttpResponseRedirect('/')
                log.info('用户： {} 注册并登录成功！'.format(username))
                request.session.set_expiry(None)  # 关闭浏览器后，session失效
                return response


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')


@login_required
def index(request):
    return render(request, "page/首页.html")


@login_required
def project(request):
    return render(request, "page/2项目管理.html")


@login_required
def project_config(request, project_id):
    from Product.models import Project
    from Autotest_platform.helper.util import get_model
    p = get_model(Project, id=project_id)
    name = p.name if p else ""
    return render(request, "page/2项目管理--环境配置.html", {"projectId": project_id, "projectName": name})


@login_required
def page(request):
    return render(request, "page/3页面管理.html")


@login_required
def element(request):
    return render(request, "page/4页面元素.html")


@login_required
def keyword(request):
    return render(request, "page/5关键字库.html")


@login_required
def keyword_create(request):
    return render(request, "page/5-1新建关键字.html")


@login_required
def keyword_edit(request, keyword_id):
    from Product.models import Keyword, Project
    from Autotest_platform.helper.util import get_model
    kw = get_model(Keyword, id=keyword_id)
    projectId = kw.projectId if kw else 0
    p = get_model(Project, id=projectId)
    projectName = p.name if projectId > 0 and p else "通用关键字封装"
    keywordName = kw.name if kw else ""
    return render(request, "page/5-2编辑关键字.html",
                  {"id": projectId, "projectName": projectName, "keywordId": keyword_id, "keywordName": keywordName})


@login_required
def testcase(request):
    return render(request, "page/6测试用例.html")


@login_required
def testcase_create(request):
    return render(request, "page/6-1新建测试用例.html")


@login_required
def testcase_edit(request, testcase_id):
    return render(request, "page/6-1编辑测试用例.html", {"testcaseId": testcase_id})


@login_required
def result(request):
    return render(request, "page/7测试结果.html")


@login_required
def result_see(request, result_id):
    return render(request, "page/7-1查看测试结果.html", {"id": result_id})


@login_required
def task(request):
    return render(request, "page/9任务管理.html")


@login_required
def loginConfig(request):
    return render(request, "page/8登录配置.html")


@login_required
def loginConfig_create(request):
    return render(request, "page/8-1新建登录配置.html")


@login_required
def loginConfig_edit(request, login_id):
    return render(request, "page/8-1编辑登录配置.html", {"id": login_id})


@login_required
def report(request, report_id):
    return render(request, "page/report.html", {"report_id": report_id})


# 400
def bad_request(request, exception, template_name='error_page/400.html'):
    log.error('-------------------->400 error<--------------------')
    return render(request, template_name)


# 403
def permission_denied(request, exception, template_name='error_page/403.html'):
    log.error('-------------------->403 error<--------------------')
    return render(request, template_name)


# 404
def page_not_found(request, exception, template_name='error_page/404.html'):
    log.error('-------------------->404 error<--------------------')
    return render(request, template_name)


# 500
def server_error(exception, template_name='error_page/500.html'):
    log.error('-------------------->500 error<--------------------')
    return render(exception, template_name)
