from django.shortcuts import render,redirect
from django.views.generic.base import View
# Create your views here.
#定义视图
from django.http import HttpRequest, HttpResponse
from .models import Grades,Students,User

def index(request):#浏览器给服务器的请求体
     # return render(request,'/admin')
     return HttpResponse("gx is a good student!")



#网页上显示班级列表
def grades(request):
    #去模板里取数据
    gradesList = Grades.objects.all()
    #将数据传递给模板，模板再渲染页面，进而将页面返回给浏览器
    return render(request,'myApp/grades.html',{"grades":gradesList})

#网页上显示学生列表
def students(request):
    studentsList = Students.objects.all()
    return render(request,"myApp/students.html",{"students":studentsList})



def gradestudents(request,num):
    grade = Grades.objects.get(pk=num)
    studentList = grade.students_set.all()
    return render(request, "myApp/students.html",{"students": studentList})



def login(request):
    # request这是前端请求发来的请求，携带的所有数据，django给我们做了一些列的处理，封装成一个对象传过来
    if request.method == 'GET':
        UserList = User.objects.all()
        return render(request,'myApp/login.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        user_obj = User.objects.filter(name=name,pwd=pwd).first()
        if user_obj:
            return redirect("/students.html")
        else:
            return HttpResponse('用户名或密码错误')

def zhuce(request):
    if request.method == 'GET':
        return render(request,'myApp/zhuce.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        re_pwd = request.POST.get('re_pwd')
        if name and pwd and re_pwd:
            if pwd == re_pwd:
                user_obj = User.objects.filter(name=name).first()
                if user_obj:
                    return HttpResponse('用户已存在')
                else:
                    User.objects.create(name=name,pwd=pwd).save()
                    return redirect('/')
            else:
                return HttpResponse('两次密码不一致')

        else:
            return HttpResponse('不能有空！')

#学生添加
def add_S(request):
    if request.method == 'GET':
        g_list = Grades.objects.all()
        return render(request,"myApp/add_S.html",{"g_list":g_list})

    elif request.method == 'POST':
        s_num = request.POST.get('snum')
        s_name = request.POST.get('sname')
        s_sex = request.POST.get('ssex')
        s_age = request.POST.get('sage')
        s_tab = request.POST.get('stab')
        s_grade = request.POST.get('sgrade')
        if(Students.objects.filter(snum=s_num).first()==None):
            Students.objects.create(
            snum = s_num,
            sname = s_name,
            ssex = s_sex,
            sage = s_age,
            stab = s_tab,
            sgrade_id = s_grade
            )
            return redirect('/students.html')
        else:
            return HttpResponse('已存在此学号！！！')


#学生信息查询
def sel_S(request):
    if request.method == 'GET':
        snum = request.GET.get('snum')
        if snum !='':
            studentsList = Students.objects.filter(snum = snum)
            return render(request,"myApp/students.html",{"students":studentsList})
        else:
            return redirect('/students.html')
#学生修改
def up_S(request):
    if request.method == 'GET':
        sid = request.GET.get('sid')
        stu = Students.objects.filter(id = sid).first()#获取列表id的信息,编辑
        g_list = Grades.objects.all()
        return render(request,"myApp/up_S.html",{'stu':stu,"g_list":g_list})

    elif request.method == 'POST':#获取修改的信息
        sid = request.POST.get('sid')
        s_num = request.POST.get('snum')
        s_name = request.POST.get('sname')
        s_sex = request.POST.get('ssex')
        s_age = request.POST.get('sage')
        s_tab = request.POST.get('stab')
        s_grade = request.POST.get('sgrade')

        Students.objects.filter(id = sid).update(
            snum=s_num,
            sname=s_name,
            ssex=s_sex,
            sage=s_age,
            stab=s_tab,
            sgrade_id=s_grade
        )
        return redirect('/students.html')

#学生信息删除
def del_S(request):
    sid = request.GET.get('sid')#sid从get请求获取
    Students.objects.filter(id=sid).delete()
    return redirect('/students.html')

#学生排序
def px_S(request):
    studentsList = Students.objects.all().order_by('sage')
    return render(request, "myApp/students.html", {"students": studentsList})

#班级添加
def add_G(request):
    if request.method == 'GET':
        return render(request,"myApp/add_G.html",)
    elif request.method == 'POST':
        g_xibie = request.POST.get('gxibie')
        g_name = request.POST.get('gname')
        g_date = request.POST.get('gdate')
        g_girlnum = request.POST.get('ggirlnum')
        g_boynum = request.POST.get('gboynum')
        if (Grades.objects.filter(gname=g_name).first() == None):
            Grades.objects.create(
                gxibie = g_xibie,
                gname = g_name,
                gdate = g_date,
                ggirlnum = g_girlnum,
                gboynum = g_boynum
            )
            return redirect('/grades.html')
        else:
            return HttpResponse('已存在此班号！！！')

#班级修改
def up_G(request):
    if request.method == 'GET':
        gid = request.GET.get('gid')
        gra = Grades.objects.filter(id = gid).first()#获取列表id的信息,编辑
        return render(request,"myApp/up_G.html",{'gra':gra})

    elif request.method == 'POST':#获取修改的信息
        gid = request.POST.get('gid')
        g_xibie = request.POST.get('gxibie')
        g_name = request.POST.get('gname')
        g_date = request.POST.get('gdate')
        g_girlnum = request.POST.get('ggirlnum')
        g_boynum = request.POST.get('gboynum')

        Grades.objects.filter(id = gid).update(
            gxibie=g_xibie,
            gname=g_name,
            gdate=g_date,
            ggirlnum=g_girlnum,
            gboynum=g_boynum
        )
        return redirect('/grades.html')

#班级信息查询
def sel_G(request):
    if request.method == 'POST':
        xb = request.POST.get('xb')
        if xb !='':
            gradesList = Grades.objects.filter(gxibie = xb)
            return render(request,"myApp/grades.html",{"grades":gradesList})
        else:
            return redirect('/grades.html')


#班级信息删除
def del_G(request):
    gid = request.GET.get('gid')
    Grades.objects.filter(id=gid).delete()
    return redirect('/grades.html')

def px_nan(request):
    gradesList = Grades.objects.all().order_by('gboynum')
    return render(request,'myApp/grades.html',{"grades":gradesList})

def px_nv(request):
    gradesList = Grades.objects.all().order_by('ggirlnum')
    return render(request,'myApp/grades.html',{"grades":gradesList})