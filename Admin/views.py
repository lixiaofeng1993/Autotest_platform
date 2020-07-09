# coding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from Autotest_platform.helper.helperPath import register_info_logic, change_info_logic, delete_testcase
from Product.models import Team, TeamUsers, ValidationError, ModularTable, Keyword, Project
from Autotest_platform.helper.util import get_model, pagination_data
from Autotest_platform.helper.Http import JsonResponse
from Product.public import check_team, model_nav, create_model
import logging

log = logging.getLogger('log')  # 初始化log


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)  # 认证给出的用户名和密码
        if user is not None and user.is_active:  # 判断用户名和密码是否有效
            auth.login(request, user)
            request.session['user'] = username  # 跨请求的保持user参数
            user_id = get_model(User, username=username).id
            request.session['user_id'] = user_id
            request.session.set_expiry(None)  # 关闭浏览器后，session失效
            response = HttpResponseRedirect('/team/')
            delete_testcase(settings.MEDIA_ROOT)
            delete_testcase(settings.LOG_PATH)
            return response
        else:
            messages.add_message(request, messages.WARNING, '账户或者密码错误，请检查')
            return render(request, 'page/1登录.html')
    elif request.method == 'GET':
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
                user_id = get_model(User, username=username).id
                request.session['user_id'] = user_id  # 将session信息记录到浏览器
                response = HttpResponseRedirect('/')
                log.info('用户： {} 注册并登录成功！'.format(username))
                request.session.set_expiry(None)  # 关闭浏览器后，session失效
                return response


@method_decorator(login_required, name='dispatch')
class TeamIndex(ListView):
    model = Team
    template_name = 'team/team.html'
    context_object_name = 'object_list'
    paginate_by = 2

    def dispatch(self, *args, **kwargs):
        return super(TeamIndex, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        team_list = get_model(Team, get=False)
        return team_list

    def get_context_data(self, **kwargs):
        self.page = self.request.GET.dict().get('page', '1')
        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        data = pagination_data(paginator, page, is_paginated)
        context.update(data)
        context.update({'page': self.page})
        return context


@login_required
def team_go(request):
    if request.method == 'POST':
        tid = request.POST.get('tid')
        user_id = request.session['user_id']
        t = TeamUsers.objects.filter(team_id=tid).filter(user_id=user_id)
        status = 0
        if len(t) == 1:
            status = t[0].status
        return JsonResponse.AbnormalCheck('要先加入团队才能进入撒~~~', data={'status': status})


@login_required
def create_team(request):
    if request.method == 'POST':
        t = Team()
        t.name = request.POST.get('name', '')
        t.remark = request.POST.get('remarks', '')
        user_id = request.session['user_id']
        t.creator = get_model(User, id=user_id)
        try:
            t.clean()
        except ValidationError as error:
            return render(request, 'team/create.html', error.message_dict)
        try:
            t.save()
        except Exception as e:
            return render(request, 'team/create.html', {'error': e.args})
        tu = TeamUsers()
        tu.team_id = t.id
        tu.user_id = t.creator_id
        tu.status = 1
        try:
            tu.save()
        except Exception as e:
            return render(request, 'team/create.html', {'error': e.args})
        return HttpResponseRedirect('/team/')
    return render(request, 'team/create.html')


@login_required
def team_edit(request, tid):
    if request.method == 'POST':
        t = get_model(Team, id=tid)
        t.name = request.POST.get('name', '')
        t.remark = request.POST.get('remarks', '')
        user_id = request.session['user_id']
        t.creator = get_model(User, id=user_id)
        try:
            t.clean()
        except ValidationError as error:
            return render(request, 'team/edit.html', error.message_dict)
        try:
            t.save()
        except Exception as e:
            return render(request, 'team/edit.html', {'error': e.args})
    te = get_model(Team, id=tid)
    user_id = request.session['user_id']
    mt = get_model(ModularTable, get=False, team_id=tid)
    if not mt:
        mt = create_model(tid)
    info = {'te': te, 'status': False, 'tid': tid, 'mt': mt.order_by('order_id')}
    if te.creator.id == user_id:
        info['status'] = True
        return render(request, 'team/edit.html', info)
    else:
        return render(request, 'team/edit.html', info)


@login_required
def team_modular(request, tid):
    if request.method == 'POST':
        mt = ModularTable()
        mt.order_id = request.POST.get('id', '')
        mt.model_name = request.POST.get('name', '')
        mt.url = request.POST.get('url', '')
        mt.Icon = request.POST.get('icon', '')
        mot = ModularTable.objects.filter(team_id=tid).filter(order_id=mt.order_id)
        if mt.order_id != 0 and mt.model_name == '0' and mt.url == '0' and mt.Icon == '0':
            try:
                mot.delete()
            except:
                pass
            return redirect('/team/edit/{}/'.format(tid))
        mt.team_id = tid
        if mot:
            mot.update(order_id=mt.order_id, model_name=mt.model_name, url=mt.url, Icon=mt.Icon)
            return redirect('/team/edit/{}/'.format(tid))
        try:
            mt.clean()
        except ValidationError as error:
            return render(request, 'team/edit.html', error.message_dict)
        try:
            mt.save()
        except Exception as e:
            return render(request, 'team/edit.html', {'error': e.args})
    return redirect('/team/edit/{}/'.format(tid))


@login_required
def team_apply(request, tid):
    if request.method == 'POST':
        apply_id = request.POST.get('apply_id')
        tu = get_model(TeamUsers, get=False, id=apply_id)
        tu.update(status=1)
        return JsonResponse.OK()
    tu = TeamUsers.objects.filter(team_id=tid).filter(status=0)
    return render(request, 'team/apply.html', {'join': tu, 'tid': tid})


@login_required
def team_join(request):
    if request.method == 'GET':
        return render(request, 'team/apply.html')
    else:
        tid = request.POST.get('tid', '')
        super_id = get_model(Team, id=tid).creator_id
        user_id = request.session.get('user_id', 0)
        if user_id == 0:
            return JsonResponse.AbnormalCheck('登录过期了呢，请重新登录~~~')
        if super_id != user_id:
            status = 0
            tus = TeamUsers.objects.filter(team_id=tid).filter(user_id=user_id)
            if tus:
                for t in tus:
                    status = t.status
                if status == 0:
                    return JsonResponse.AbnormalCheck('申请已提交，等待管理员审核中~~~')
                else:
                    return JsonResponse.OK('申请已通过，赶快进入体验吧~~~')
            else:
                tu = TeamUsers()
                tu.team = get_model(Team, id=tid)
                tu.user = get_model(User, id=user_id)
                try:
                    tu.save()
                except Exception as e:
                    return JsonResponse.AbnormalCheck('申请失败！{}'.format(e))
                return JsonResponse.OK('申请成功，等待管理员审核中~~~')
        else:
            return JsonResponse.SkipLink()


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')


@login_required
def index(request, tid):
    t = get_model(Team, id=tid)
    if not t:
        return redirect('/team/')
    request.session['tid'] = tid
    model_list = get_model(ModularTable, get=False, team_id=tid).order_by('order_id')
    return render(request, 'page/首页.html', {'tid': tid, 'model_list': model_list})


@login_required
@check_team
def project(request):
    tid, model_list = model_nav(request)
    return render(request, 'page/2项目管理.html', {'tid': tid, 'model_list': model_list})


@login_required
@check_team
def project_config(request, project_id):
    p = get_model(Project, id=project_id)
    name = p.name if p else ''
    tid, model_list = model_nav(request)
    info = {'projectId': project_id, 'projectName': name, 'tid': tid, 'model_list': model_list}
    return render(request, 'page/2项目管理--环境配置.html', info)


@login_required
@check_team
def page(request):
    tid, model_list = model_nav(request)
    return render(request, 'page/3页面管理.html', {'tid': tid, 'model_list': model_list})


@login_required
@check_team
def element(request):
    project_id = request.GET.get('projectId', 'false')
    page_id = request.GET.get('pageId', 'false')
    tid, model_list = model_nav(request)
    info = {'projectId': project_id, 'pageId': page_id, 'tid': tid, 'model_list': model_list}
    return render(request, 'page/4页面元素.html', info)


@login_required
@check_team
def keyword(request):
    tid, model_list = model_nav(request)
    return render(request, 'page/5关键字库.html', {'tid': tid, 'model_list': model_list})


@login_required
@check_team
def keyword_create(request):
    tid, model_list = model_nav(request)
    return render(request, 'page/5-1新建关键字.html', {'tid': tid, 'model_list': model_list})


@login_required
@check_team
def keyword_edit(request, keyword_id):
    kw = get_model(Keyword, id=keyword_id)
    project_id = kw.project_id if kw else 0
    p = get_model(Project, id=project_id)
    project_name = p.name if project_id is not None and p else '通用关键字封装'
    keyword_name = kw.name if kw else ''
    tid, model_list = model_nav(request)
    info = {'id': project_id, 'projectName': project_name, 'keywordId': keyword_id, 'keywordName': keyword_name,
            'tid': tid, 'model_list': model_list}
    return render(request, 'page/5-2编辑关键字.html', info)


@login_required
@check_team
def testcase(request):
    tid, model_list = model_nav(request)
    return render(request, 'page/6测试用例.html', {'tid': tid, 'model_list': model_list})


@login_required
@check_team
def testcase_create(request):
    tid, model_list = model_nav(request)
    return render(request, 'page/6-1新建测试用例.html', {'tid': tid, 'model_list': model_list})


@login_required
@check_team
def testcase_edit(request, testcase_id):
    tid, model_list = model_nav(request)
    info = {'testcaseId': testcase_id, 'tid': tid, 'model_list': model_list}
    return render(request, 'page/6-1编辑测试用例.html', info)


@login_required
@check_team
def result(request):
    tid, model_list = model_nav(request)
    return render(request, 'page/7测试结果.html', {'tid': tid, 'model_list': model_list})


@login_required
@check_team
def result_see(request, result_id):
    tid, model_list = model_nav(request)
    return render(request, 'page/7-1查看测试结果.html', {'id': result_id, 'tid': tid, 'model_list': model_list})


@login_required
@check_team
def task(request):
    tid, model_list = model_nav(request)
    return render(request, 'page/9任务管理.html', {'tid': tid, 'model_list': model_list})


@login_required
@check_team
def loginConfig(request):
    tid, model_list = model_nav(request)
    return render(request, 'page/8登录配置.html', {'tid': tid, 'model_list': model_list})


@login_required
@check_team
def loginConfig_create(request):
    tid, model_list = model_nav(request)
    return render(request, 'page/8-1新建登录配置.html', {'tid': tid, 'model_list': model_list})


@login_required
@check_team
def loginConfig_edit(request, login_id):
    tid, model_list = model_nav(request)
    return render(request, 'page/8-1编辑登录配置.html', {'id': login_id, 'tid': tid, 'model_list': model_list})


# @login_required
# def report(request, report_id):
#
#     return render(request, 'page/report.html', {'report_id': report_id})


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


@login_required
def change_password(request):
    '''
    修改密码
    :param request:
    :return:
    '''
    if request.method == 'POST':
        new_password = request.POST.get('new_password', '')
        user = request.POST.get('user', '')

        msg = change_info_logic(new_password)
        if msg != 'ok':
            log.error('change password error：{}'.format(msg))
            return JsonResponse({'msg': msg})
        else:
            user = User.objects.get(username=user)
            user.set_password(new_password)
            user.save()
            log.info('用户：{} 修改密码为 {}'.format(user, new_password))
            return JsonResponse({'msg': 'success'})


def delete_customer(request, phone):
    import re
    from Autotest_platform.helper.connectMySql import SqL

    patt = re.compile('^1[3-8]\d{9}$')
    ver = patt.findall(str(phone))
    if not ver:
        return JsonResponse.AbnormalCheck('手机号输入不符合规则，请重新输入!')
    sql = SqL(job=True)
    sql_ = SqL()
    try:
        customer_id = sql.execute_sql('SELECT id FROM customer WHERE phone = "{}" AND channel_id =1;'.format(phone))
        msg1 = sql.execute_sql('DELETE FROM wechat_user WHERE customer_id = "{}";'.format(customer_id))
        msg2 = sql.execute_sql('DELETE FROM account WHERE customer_id = "{}";'.format(customer_id))
        msg3 = sql.execute_sql('DELETE FROM customer_vip_info WHERE customer_id = "{}";'.format(customer_id))
        msg4 = sql.execute_sql('DELETE FROM customer_attachment_info WHERE customer_id = "{}";'.format(customer_id))
        msg5 = sql.execute_sql('DELETE FROM customer WHERE id = "{}";'.format(customer_id))
        msg6 = sql.execute_sql('DELETE FROM balance_account WHERE account = "{}" AND channel_id = 1;'.format(phone))

        easy_agent_id = sql_.execute_sql('SELECT easy_agent_id FROM easy_agent WHERE phone = "{}";'.format(phone))
        msg7 = sql_.execute_sql(
            'DELETE FROM easy_agent_account WHERE easy_agent_id  = "{}";'.format(easy_agent_id))
        msg8 = sql_.execute_sql(
            'DELETE FROM easy_agent WHERE easy_agent_id  = "{}";'.format(easy_agent_id))

        log.info(
            '返回值：{}, {}, {}, {}, {},{}, {}, {}'.format(customer_id, msg1, msg2, msg3, msg4, msg5, msg6, msg7, msg8))
        if not msg1 and not msg2 and not msg3 and not msg4 and not msg5 and not msg6 and not msg7 and not msg8:
            return JsonResponse.OK('删除用户：{} 成功！'.format(phone))
        else:
            return JsonResponse.ServerError(msg1 + msg2 + msg3 + msg4 + msg5 + msg6 + msg7 + msg8)
    except Exception as e:
        return JsonResponse.ServerError('删除用户出现错误：{}'.format(e))


def set_balance(request, phone):
    import re
    from Autotest_platform.helper.connectMySql import SqL

    patt = re.compile('^1[3-8]\d{9}$')
    ver = patt.findall(str(phone))
    if not ver:
        return JsonResponse.AbnormalCheck('手机号输入不符合规则，请重新输入!')
    balance = request.GET.get('balance', '')
    patt1 = re.compile('^\d{3,6}$')
    ver1 = patt1.findall(str(balance))
    if not ver1:
        return JsonResponse.AbnormalCheck('输入的余额不符合规则，请重新输入!')
    sql = SqL()
    try:
        easy_agent_id = sql.execute_sql('SELECT easy_agent_id FROM easy_agent WHERE phone = "{}";'.format(phone))
        msg = sql.execute_sql(
            'update easy_agent_account set balance= "{}" where easy_agent_id = "{}";'.format(balance, easy_agent_id))
        log.info('返回值：{}, {}'.format(easy_agent_id, msg))
        if not msg:
            return JsonResponse.OK('用户：{} 设置余额：{} 成功！'.format(phone, balance))
    except Exception as e:
        return JsonResponse.ServerError('用户：{} 设置余额出现错误！{}'.format(phone, e))
