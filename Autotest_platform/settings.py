"""
Django settings for Autotest_platform project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import djcelery
from celery.schedules import crontab
from datetime import timedelta

djcelery.setup_loader()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#zpo_me0s492$q_8-2qav%53jx+965%3qx9j0eyqzf8yx=%%rr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']
ALLOWED_HOSTS = ['*', '192.168.1.3', 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'Product',
    'Admin',
]

# AUTH_USER_MODEL = 'Product.User'

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Autotest_platform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Autotest_platform.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'autotest',
        'NAME': 'easy',
        'USER': 'root',
        'PASSWORD': '123456',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672'
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
# BROKER_URL = 'amqp://guest:guest@localhost:5672'
# CELERY_RESULT_BACKEND = 'amqp://guest:guest@localhost:5672'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# 上传
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 对应文件夹
if not os.path.exists(MEDIA_ROOT): os.mkdir(MEDIA_ROOT)
MEDIA_URL = '/media/'  # 对应上线后的url

import djcelery

djcelery.setup_loader()
BROKER_URL = 'redis://127.0.0.1:6379/0'
# broker_pool_limit=None
# BROKER_POOL_LIMIT=None
CELERY_IMPORTS = ('Product.tasks')
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_ENABLE_UTC = False
CELERYBEAT_SCHEDULE = {
    # 'timing': {
    #     'task': 'Product.tasks.timingRunning',
    #     # 'schedule': crontab(hour=10, minute=30),
    #     'schedule': timedelta(seconds=300),
    # },
}

# log
import time

LOG_PATH = os.path.join(BASE_DIR, 'logs')  # 对应文件夹
if not os.path.exists(LOG_PATH): os.mkdir(LOG_PATH)  # 如果不存在这个logs文件夹，就自动创建一个

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        # 日志格式
        'standard': {
            'format': '[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] '
                      '[%(levelname)s]- %(message)s'},
        'simple': {  # 简单格式
            'format': '%(levelname)s %(message)s'
        },
    },
    # 过滤
    'filters': {
    },
    # 定义具体处理日志的方式
    'handlers': {
        # 默认记录所有日志
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH, 'all-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码
        },
        # 输出错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH, 'error-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码
        },
        # 控制台输出
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        # 输出info日志
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH, 'info-{}.log'.format(time.strftime('%Y-%m-%d'))),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',  # 设置默认编码
        },
    },
    # 配置用哪几种 handlers 来处理日志
    'loggers': {
        # 类型 为 django 处理所有类型的日志， 默认调用
        'django': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': False
        },
        # log 调用时需要当作参数传入
        'log': {
            'handlers': ['error', 'info', 'console', 'default'],
            'level': 'INFO',
            'propagate': True
        },
    }
}

# 未登录重定向地址
LOGIN_URL = "/login/"

# simpleui 设置

# 首页配置
# SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'
# 首页标题
# SIMPLEUI_HOME_TITLE = '百度一下你就知道'
# 首页图标,支持element-ui的图标和fontawesome的图标
# SIMPLEUI_HOME_ICON = 'el-icon-date'

# 设置simpleui 点击首页图标跳转的地址
# SIMPLEUI_INDEX = 'https://www.88cto.com'

# 首页显示服务器、python、django、simpleui相关信息
# SIMPLEUI_HOME_INFO = True

# 首页显示快速操作
SIMPLEUI_HOME_QUICK = True

# 首页显示最近动作
SIMPLEUI_HOME_ACTION = True

# 自定义SIMPLEUI的Logo
# SIMPLEUI_LOGO = 'https://avatars2.githubusercontent.com/u/13655483?s=60&v=4'

# 登录页粒子动画，默认开启，False关闭
# SIMPLEUI_LOGIN_PARTICLES = False

# 让simpleui 不要收集相关信息
# SIMPLEUI_ANALYSIS = True

# 自定义simpleui 菜单
SIMPLEUI_CONFIG = {
    # 在自定义菜单的基础上保留系统模块
    # 'system_keep': False,
    'system_keep': True,
    'menus': [
        {
            'app': ' auth',
            'name': '账户管理',
            # 'icon': 'fas fa-user-shield',
            'models': [{
                'name': '用户',
                'icon': 'fa fa-user',
                'url': 'auth/user/'
            }, {
                'name': '组',
                'icon': 'fas fa-users-cog',
                'url': 'auth/group/'
            }
            ]
        },
        {
            'app': 'Product',
            'name': '测试平台',
            # 'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': '项目管理',
                    # 'icon': 'fa fa-product-hunt fa-fw',
                    'url': 'Product/project/'
                },
                {
                    'name': '页面管理',
                    # 'icon': 'fa fa-product-hunt fa-fw',
                    'url': 'Product/page/'
                },
                {
                    'name': '页面元素',
                    # 'icon': 'fa fa-product-hunt fa-fw',
                    'url': 'Product/element/'
                },
                {
                    'name': '关键字库',
                    # 'icon': 'fa fa-product-hunt fa-fw',
                    'url': 'Product/keyword/'
                },
                {
                    'name': '测试用例',
                    # 'icon': 'fa fa-product-hunt fa-fw',
                    'url': 'Product/testcase/'
                },
                {
                    'name': '测试结果',
                    # 'icon': 'fa fa-product-hunt fa-fw',
                    'url': 'Product/result/'
                },
                {
                    'name': '登录配置',
                    # 'icon': 'fa fa-product-hunt fa-fw',
                    'url': 'Product/loginconfig/'
                }, {
                    'name': '任务管理',
                    # 'icon': 'fa fa-product-hunt fa-fw',
                    'url': 'Product/task/'
                },
            ]
        },
    ]
}
# 是否显示默认图标，默认=True
# SIMPLEUI_DEFAULT_ICON = False

# 图标设置，图标参考：
SIMPLEUI_ICON = {
    # '测试平台': 'fab fa-apple',
    # '账户管理': 'fas fa-user-tie'
}

# 指定simpleui 是否以脱机模式加载静态资源，为True的时候将默认从本地读取所有资源，即使没有联网一样可以。适合内网项目
# 不填该项或者为False的时候，默认从第三方的cdn获取

SIMPLEUI_STATIC_OFFLINE = True
