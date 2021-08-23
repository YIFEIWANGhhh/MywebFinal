from django.contrib import admin
from myapp.models import Team, FormName, Task, info

@admin.register(Team)


# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id','name','peopleNb')
    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 10
    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  #-id降序


@admin.register(Task)
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id','wbsNb', 'description','projectType')
    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 10
    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  #-id降序
    search_fields = ['wbsNb']







@admin.register(info)
# Register your models here.
class infoAdmin(admin.ModelAdmin):
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = (
    'get_projecttype','get_wbsnb','otherDepartement','get_description','taskDescription','startTime',
    'endTime','peopleNb','workHours','formName')
    list_filter = ('formName','wbsNb__projectType','team__name')
    # fields = (
    # 'wbsNb__projectType','wbsNb__wbsNb','otherDepartement','wbsNb__description','taskDescription','startTime',
    # 'endTime','peopleNb','workHours')


    # list_display = (
    # 'wbsNb', 'otherDepartement', 'taskDescription', 'startTime',
    # 'endTime', 'peopleNb', 'workHours')
    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20
    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  #-id降序
    autocomplete_fields = ['wbsNb']

    def get_description(self, obj):
        return obj.wbsNb.description        # 这是我们要展示的字段
    get_description.short_description = '任务内容'
    get_description.admin_order_field = 'wbsNb.description'
    def get_wbsnb(self, obj):
        return obj.wbsNb.wbsNb        # 这是我们要展示的字段
    get_wbsnb.short_description = 'WBS编号'
    get_wbsnb.admin_order_field = 'wbsNb'
    def get_projecttype(self,obj):
        return obj.wbsNb.projectType
    get_projecttype.short_description = '项目型号'
    get_projecttype.admin_order_field = 'projecttype'

# class infoInline(admin.StackedInline):
#     model = info


@admin.register(FormName)
# Register your models here.
class FormNameAdmin(admin.ModelAdmin):
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id','name','workdays')
    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 10
    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  #-id降序
    #inlines = [infoInline, ]

