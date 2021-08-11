from django.db import models


# Create your models here.
class Team(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField("团队", max_length=255)
    peopleNb = models.IntegerField("人数")
    def __str__(self):
        return "%s:%c"%(self.name, self.peopleNb)

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    wbsNb = models.CharField("WBS/WP编号", max_length=255)
    description = models.CharField("任务内容", max_length=255)
    projectType = models.CharField("型号", max_length=255)
    def __str__(self):
        return "%s:%s:%s"%(self.wbsNb, self.description, self.projectType)

class FormName(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("表名", max_length=255)
    days = models.IntegerField("工作日")
    def __str__(self):
        return "%s"%(self.name)

class info(models.Model):
    id = models.AutoField(primary_key=True)
    peopleNb = models.IntegerField("人数")
    workHours = models.IntegerField("工时")
    taskDescription = models.CharField("任务说明", max_length=255, blank= True)
    startTime = models.DateField("开始时间")
    endTime = models.DateField("结束时间")
    otherDepartement = models.CharField("承接部门", max_length=255, blank= True)
    wbsNb = models.ForeignKey('Task', on_delete=models.CASCADE,verbose_name="WBS编号")
    team = models.ForeignKey('Team', on_delete=models.CASCADE,verbose_name="团队")
    formName = models.ForeignKey('FormName', on_delete=models.CASCADE,verbose_name="表名")

    def __str__(self):
        return "%s:%s:%s" % (self.team.name, self.formName.name,self.wbsNb.wbsNb)





