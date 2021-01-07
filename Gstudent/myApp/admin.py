from django.contrib import admin

# Register your models here.
from .models import Grades,Students,User

#注册
#admin.site.register(Grades)
#admin.site.register(Students)

#设置标语
admin.site.site_header = '学生管理系统'
admin.site.site_title = '440系统'
admin.site.index_title = '欢迎使用学生管理系统'

'''
class StudentsInfo(admin.TabularInline):#StackedInline
    model = Students
    extra = 2
'''

#添加班级信息
class GradesAdmin(admin.ModelAdmin):
    #inlines = [StudentsInfo]
    #列表页属性
    list_display = ['pk','gxibie','gname','gdate','ggirlnum','gboynum']#显示字段
    list_filter = ['gname']#过滤字段
    search_fields = ['gname']#搜索字段
    list_per_page = 5#分页

    # 添加、修改页属性
    # fields = ['ggirlnum','gboynum','gname','gdata','isDeleete']
    fieldsets = [
        ('num', {'fields': ['ggirlnum', 'gboynum']}),
        ('base', {'fields': ['gxibie','gname', 'gdate']})
    ]
admin.site.register(Grades, GradesAdmin)

#布尔值显示问题,使用修饰器完成注册
class StudentsAdmin(admin.ModelAdmin) :
# 设置页面列的名称
    list_display = ['pk', 'snum','sname', 'ssex','sage', 'stab','sgrade']
    list_per_page = 5
    actions_on_bottom = True
    actions_on_top = False
#设置搜索框
    search_fields = ['sname']
admin.site.register(Students, StudentsAdmin)

#设置后台注册
class LoginAdmin(admin.ModelAdmin):
    list_display = ['id','name','pwd']
    list_per_page = 5
admin.site.register(User, LoginAdmin)



