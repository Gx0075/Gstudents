from django.conf.urls import url
from django.conf import settings
from.import views
urlpatterns =[
    url(r'^$',views.login),
    url(r'^zhuce',views.zhuce),
    #班级和学生主页面
    url(r'^grades',views.grades),
    url(r'^students',views.students),

    #学生信息的添加，修改
    url(r'^add_S',views.add_S),
    url(r'^up_S',views.up_S),
    url(r'^del_S',views.del_S),
    url(r'^sel_S',views.sel_S),
    url(r'px_S',views.px_S),

    #班级信息的添加，修改
    url(r'^add_G',views.add_G),
    url(r'^up_G',views.up_G),
    url(r'^del_G',views.del_G),
    url(r'^sel_G',views.sel_G),
    url(r'^px_nan',views.px_nan),
    url(r'^px_nv',views.px_nv)


]