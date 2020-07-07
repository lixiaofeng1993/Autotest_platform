from django.http import HttpResponse
import json
import logging

log = logging.getLogger('log')  # 初始化log


class JsonResponse(HttpResponse):
    def __init__(self, code=200, message='ok', data=None):
        response = dict()
        response['code'] = code
        response['message'] = message
        response['data'] = data
        super(JsonResponse, self).__init__(json.dumps(response, ensure_ascii=False), content_type='application/json', )
        self['Access-Control-Allow-Origin'] = '*'
        self['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
        self['Access-Control-Max-Age'] = '1000'
        self['Access-Control-Allow-Headers'] = '*'
        self['Accept'] = '*'

    @staticmethod
    def OK(message='ok', data=None):
        log.info('执行成功！{}'.format(message))
        response = JsonResponse(200, message, data)
        return response

    @staticmethod
    def BadRequest(message='Bad request', data=None):
        log.warning('执行出现异常！{}'.format(message))
        response = JsonResponse(400, message, data)
        return response

    @staticmethod
    def Unauthorized(message='Unauthorized', data=None):
        log.warning('未授权！{}'.format(message))
        return JsonResponse(401, message, data)

    @staticmethod
    def MethodNotAllowed(message='Method not allowed', data=None):
        log.warning('不允许的方法！{}'.format(message))
        return JsonResponse(405, message, data)

    @staticmethod
    def ServerError(message='Internal server error', data=None):
        log.error('服务异常！{}'.format(message))
        return JsonResponse(500, message, data)

    @staticmethod
    def SkipLink(message='skip link', data=None):
        log.warning('跳转链接！{}'.format(message))
        return JsonResponse(403, message, data)

    @staticmethod
    def AbnormalCheck(message='except check', data=None):
        log.warning('异常检查！{}'.format(message))
        return JsonResponse(999, message, data)


class Session:
    USER = 'user'


# 检查请求是否为Post请求
def post(fn):
    def request(*args, **kwargs):
        if args[0].method == 'POST':
            return fn(*args, **kwargs)
        else:
            return JsonResponse.MethodNotAllowed('请使用Post请求')

    return request


#  检查请求是否携带登陆信息
def check_login(fn):
    def _check_login(*args, **kwargs):
        try:
            if not (args[0].session.get(Session.USER, None)):
                return JsonResponse.Unauthorized('未检测到登陆信息')
            return fn(*args, **kwargs)
        except:
            return JsonResponse.ServerError('检查登陆状态时出错')

    return _check_login


def get_request_body(request):
    try:
        content = request.body.decode()
        content = json.loads(request.body.decode('utf-8')) if content else {}
    except:
        raise ValueError
    return content
