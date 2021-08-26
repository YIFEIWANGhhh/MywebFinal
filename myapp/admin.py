from django.contrib import admin
from myapp.models import Team, FormName, Task, info
from openpyxl import Workbook
from django.shortcuts import render,HttpResponse,redirect
import xlwt
import os
from io import BytesIO
admin.site.site_header = "人工时填报系统数据管理"
class ExportExcelMixin(object):

    def export_as_excel(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='application/msexcel')
        response['Content-Disposition'] = f'attachment; filename={meta}.xlsx'
        wb = Workbook()
        ws = wb.active
        ws.append(field_names)
        for obj in queryset:
            for field in field_names:
                data = [f'{getattr(obj, field)}' for field in field_names]
            row = ws.append(data)
        wb.save(response)
        return response

    export_as_excel.short_description = '导出Excel'

@admin.register(Team)
# Register your models here.
class TeamAdmin(admin.ModelAdmin,ExportExcelMixin):
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id','name','peopleNb')
    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 10
    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  #-id降序
    actions = ['export_as_excel']


@admin.register(Task)
# Register your models here.
class TaskAdmin(admin.ModelAdmin, ExportExcelMixin):
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id','wbsNb', 'description','projectType')
    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 10
    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  #-id降序
    search_fields = ['wbsNb']
    actions = ["export_as_excel"]



@admin.register(info)
# Register your models here.
class infoAdmin(admin.ModelAdmin):
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = (
    'get_projecttype','get_wbsnb','otherDepartement','get_description','taskDescription','startTime',
    'endTime','peopleNb','workHours','formName')
    list_filter = ('formName','wbsNb__projectType','team__name')
    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20
    #ordering设置默认排序字段，负号表示降序排序
    #ordering = ('id')  #-id降序
    autocomplete_fields = ['wbsNb']
    actions = ["export_as_excel"]
    def export_as_excel(self, request, queryset):
        style = xlwt.XFStyle()
        list_obj = queryset
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment;filename=info.xls'
        if list_obj:
            ws = xlwt.Workbook(encoding='utf-8')
            w = ws.add_sheet('sheet1')
            w.write(0,0,u'表名')
            w.write(0,1,u'团队')
            w.write(0,2,u'型号')
            w.write(0,3,u'WBS/WP编号')
            w.write(0,4,u'任务委托部门')
            w.write(0,5,u'任务内容')
            w.write(0,6,u'任务内容说明')
            w.write(0,7,u'开始时间', style)
            w.write(0,8,u'完成时间',style)
            w.write(0,9,u'人数')
            w.write(0,10,u'工时/人')
            w.write(0,11,u'备注')
            excel_row = 1
            for obj in list_obj:
                formname = obj.formName.name
                team = obj.team.name
                projecttype = obj.wbsNb.projectType
                WBS = obj.wbsNb.wbsNb
                otherdepartement = obj.otherDepartement
                description = obj.wbsNb.description
                taskdescription = obj.taskDescription
                starttime = obj.startTime.strftime('%Y-%m-%d')
                endtime = obj.endTime.strftime('%Y-%m-%d')
                peoplenb = obj.peopleNb
                workhours = obj.workHours
                remark = obj.remark
                w.write(excel_row,0,formname)
                w.write(excel_row,1,team)
                w.write(excel_row,2,projecttype)
                w.write(excel_row,3,WBS)
                w.write(excel_row,4,otherdepartement)
                w.write(excel_row,5,description)
                w.write(excel_row,6,taskdescription)
                w.write(excel_row,7,starttime)
                w.write(excel_row,8,endtime)
                w.write(excel_row,9,peoplenb)
                w.write(excel_row,10,workhours)
                w.write(excel_row,11,remark)
                excel_row +=1
            output = BytesIO()
            ws.save(output)
            output.seek(0)
            response.write(output.getvalue())
        return response
    export_as_excel.short_description = '导出Excel'


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
