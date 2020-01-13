from django.contrib import admin
from Product.models import Project, Page, Element, Keyword, TestCase, Result, Task, LoginConfig


class ProjectAdmin(admin.ModelAdmin):
    # list_display 字段名称的数组，定义要在列表中显示的字段 search_fields 设置搜索关键字匹配 list_filter 表字段过滤器
    list_display = ['id', 'name', 'creator', 'remark', 'createTime']
    search_fields = ['name', 'id']  # 搜索栏
    list_filter = ['creator']  # 过滤器


class PageAdmin(admin.ModelAdmin):
    list_display = ['id', 'projectId', 'name', 'remark', 'createTime']
    search_fields = ['id', 'name']  # 搜索栏
    list_filter = ['name']  # 过滤器


class ElementAdmin(admin.ModelAdmin):
    list_display = ['id', 'projectId', 'pageId', 'name', 'by', 'locator', 'remark', 'createTime']
    search_fields = ['id', 'name']  # 搜索栏
    list_filter = ['name']  # 过滤器


class KeywordAdmin(admin.ModelAdmin):
    list_display = ['id', 'projectId', 'name', 'type', 'method', 'params', 'remark', 'createTime']
    search_fields = ['id', 'name']  # 搜索栏
    list_filter = ['name']  # 过滤器


class TestCasedAdmin(admin.ModelAdmin):
    list_display = ['id', 'projectId', 'title', 'level', 'beforeLogin', 'remark', 'createTime']
    search_fields = ['id', 'title']  # 搜索栏
    list_filter = ['title']  # 过滤器


class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'browsers', 'beforeLogin', 'environments', 'status', 'createTime']
    search_fields = ['id', 'title']  # 搜索栏
    list_filter = ['title']  # 过滤器


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'testcases', 'browsers', 'status', 'remark', 'createTime']
    search_fields = ['id', 'name']  # 搜索栏
    list_filter = ['name']  # 过滤器


class LoginConfigAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'projectId', 'remark', 'createTime']
    search_fields = ['id', 'name']  # 搜索栏
    list_filter = ['name']  # 过滤器


admin.site.register(Project, ProjectAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Element, ElementAdmin)
admin.site.register(TestCase, TestCasedAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(LoginConfig, LoginConfigAdmin)
admin.site.register(Keyword, KeywordAdmin)
