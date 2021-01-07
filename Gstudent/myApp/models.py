from django.db import models

# Create your models here.
class Grades(models.Model):
    gxibie = models.CharField(verbose_name='所属系别',max_length=20)
    gname = models.CharField(verbose_name='班级班号',max_length=20)
    gdate = models.DateField(verbose_name='创建日期')
    ggirlnum = models.IntegerField(verbose_name='女生人数')
    gboynum = models.IntegerField(verbose_name='男生人数')

class Students(models.Model):
    snum = models.CharField(verbose_name='学生学号',max_length=20)
    sname = models.CharField(verbose_name='学生姓名',max_length=20)
    ssex = models.CharField(verbose_name='学生性别',max_length=20)
    sage = models.IntegerField(verbose_name='学生年龄')
    stab = models.CharField(verbose_name='联系方式',max_length=20)
    sgrade = models.ForeignKey("Grades",verbose_name='所属班级',on_delete=models.CASCADE)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='账号',max_length=32)
    pwd = models.CharField(verbose_name='密码',max_length=32)