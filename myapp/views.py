from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from myapp.models import Team, FormName,info,Task
import json



# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the myapp index.")
def index(request):
    return render(request,'myapp/index.html')


"""
    team功能描述:
        获取所有team的name并返回
    Args: 
        
    Returns:
        mylist: dict 
"""
def team(request):
    #获取所有team表的信息
    dlist = Team.objects.all()
    mylist = []
    for ob in dlist:
        mylist.append({'id': ob.id,'name':ob.name})
    return JsonResponse({'data': mylist})


"""
    task功能描述:
        获取所有task的wbsnb值并返回
    Args: 
        
    Returns:
        mylist: dict 
"""
def task(request):
    #获取所有task表信息
    dlist = Task.objects.all()
    mylist = []
    for ob in dlist:
        mylist.append({'id': ob.id,'wbsNb':ob.wbsNb})
    return JsonResponse({'data': mylist})


"""
    formname功能描述:
        获取所有team的name并返回
    Args: 
        
    Returns:
        mylist: dict 
"""
def formname(request):
    #获取所有team表的信息
    dlist = FormName.objects.all()
    mylist = []
    for ob in dlist:
        mylist.append({'id': ob.id,'name':ob.name})
    return JsonResponse({'data': mylist})


"""
    get_description功能描述:
        根据wbsnb编号，返回任务描述和任务型号
    Args: 
        wbsnb: str
    Returns:
        mylist: dict 
"""
def get_description(request, wbsnb):

    dlist = Task.objects.filter(wbsNb=wbsnb)
    mylist = []
    for ob in dlist:
        mylist.append({'id': ob.id,'description':ob.description,'projecttype':ob.projectType})
    return JsonResponse({'data': mylist})


"""
    get_info功能描述:
        根据表名，返回info的信息
    Args: 
        tablename: str
    Returns:
        mylist: dict 
"""
def get_info(request, tablename):
    dlist =info.objects.filter(formName__name=tablename)
    mylist = []
    for ob in dlist:
        mylist.append({'id': ob.id,'peopleNb':ob.peopleNb,'workhours':ob.workHours,
                       'team':ob.team.name, 'taskdescription':ob.taskDescription, 'starttime':ob.startTime,
                       'endtime':ob.endTime,'otherdepartement':ob.otherDepartement,'remark':ob.remark,'wbsNb':ob.wbsNb.wbsNb,
                       'description': ob.wbsNb.description,'projecttype':ob.wbsNb.projectType})
    return JsonResponse({'data': mylist})







def test(request):
    return render(request,'myapp/test.html')
def test2(request):
    return render(request,'myapp/test2.html')


def upload(request):
    if request.method=="POST":
        peoplenb = request.POST.get('peoplenb')
        workhours = request.POST.get('workhours')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        description = request.POST.get('description')
        content = request.POST.get('content')
        otherdepartement = request.POST.get('otherdepartement')
        wbs = request.POST.get('select_wbsnb')
        projecttype = request.POST.get('select_projecttype')
        team = request.POST.get('select_team')
        print(peoplenb,workhours,start_time,end_time,
              description,content,otherdepartement,wbs,
              projecttype,team)

    return HttpResponse("ok")



"""
    test1功能描述:
        将数据插入数据库
    Args: 
    
    Returns:
        ok页面 
"""
def test1(request):
    mod = info()
    mod.workHours=31
    mod.peopleNb = 10
    mod.taskDescription = "做好了????"
    mod.otherDepartement="工程中心"
    mod.startTime = "2021-3-4"
    mod.endTime = "2021-7-5"

    t = Team.objects.get(name="机械加工")
    mod.team = t
    f = FormName.objects.get(name="2021.03")
    mod.formName = f
    w = Task.objects.get(wbsNb="ZC1A1020205")
    mod.wbsNb = w
    mod.save()
    return HttpResponse("ok")




"""
    uploadtest2功能描述:
        将接收到的数据，处理，并打印出来
    Args: 
    Returns:
        test2页面 
"""
def uploadtest2(request):
    if request.method == "POST":
        data = request.POST.get("total_data")
        data_clean = data.split('#')
        data_clean.pop()
        for i in data_clean:
            j = i.split(',')
            print(j)
            remark = j[12]
            peoplenb = j[9]
            workhours = j[10]
            start_time = j[7]
            end_time = j[8]
            content = j[6]
            description = j[5]
            otherdepartement = j[4]
            wbs = j[3]
            projecttype = j[1]
            team = j[2]
            formname = j[0]
            #print(projecttype,team,wbs,otherdepartement,description,content,start_time,end_time,peoplenb,workhours,remark)
            insert_info(team,formname,wbs,peoplenb,workhours,start_time,end_time,content,otherdepartement,remark)
    return render(request,'myapp/test2.html')




"""
    uploadtest2功能描述:
        将数据，插入数据库
    Args: 
    team： str
    formname:   str 
    wbs:    str
    peoplenb:   int
    workhours:  int
    start_time: date
    end_time:   date
    content:    str
    otherdepartement:   str
    remark: str
    Returns:
"""
def insert_info(team,formname,wbs,peoplenb,workhours,start_time,end_time,
                content,otherdepartement,remark):
    mod = info()
    mod.workHours= workhours
    mod.peopleNb = peoplenb
    mod.taskDescription = content
    mod.otherDepartement= otherdepartement
    mod.startTime = start_time
    mod.endTime = end_time
    mod.remark = remark
    t = Team.objects.get(name=team)
    mod.team = t
    f = FormName.objects.get(name=formname)
    mod.formName = f
    w = Task.objects.get(wbsNb=wbs)
    mod.wbsNb = w
    mod.save()

def edit(request, info_id):
    ob = info.objects.get(id=info_id)
    context = {"info": ob}
    return render(request, "myapp/edit.html", context)

def edit_upload(request):
    uid = request.POST['id']
    ob = info.objects.get(id=uid)
    ob.peopleNb = request.POST['peoplenb']
    ob.workHours = request.POST['workhours']
    ob.remark = request.POST['remark']
    ob.otherDepartement = request.POST['otherdepartement']
    ob.taskDescription = request.POST['taskdescription']
    ob.startTime = request.POST['starttime']
    ob.endTime = request.POST['endtime']
    ob.save()
    context = {"info":"edit success"}

    return render(request,"myapp/test2.html",context)
