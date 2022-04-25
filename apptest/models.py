from django.db import models

# Create your models here.
class UserInfo(models.Model):
    """用户表"""
    name=models.CharField(verbose_name='姓名',max_length=32)
    password=models.CharField(verbose_name='密码',max_length=64)
    age=models.IntegerField(verbose_name='年龄')
    account=models.DecimalField(verbose_name='账号余额',max_digits=10,decimal_places=2,default=0)
    create_time=models.DateField(verbose_name='入职时间',null=True)
    #部门级联删除
    depart=models.ForeignKey(verbose_name='部门',to='Department',to_field='id',on_delete=models.CASCADE,default=0)

    ganer_choice=((1,"男"),(2,"女"))
    gender=models.SmallIntegerField(verbose_name="性别",choices=ganer_choice)

class Department(models.Model):
    """部门表"""
    title=models.CharField(verbose_name='部门',max_length=32)

    def __str__(self):
        return self.title

class Phone(models.Model):
    """靓号表"""
    mobile=models.CharField(verbose_name="靓号",max_length=11)
    price=models.IntegerField(verbose_name="价格")
    level_choice=((1,"1级"),(2,"2级"),(3,"3级"))
    level=models.SmallIntegerField(verbose_name="级别",choices=level_choice)
    status_choice=((1,"未占用"),(2,"已占用"))
    status=models.SmallIntegerField(verbose_name="状态",choices=status_choice,default=1)

class Admins(models.Model):
    """管理员表"""
    adminname=models.CharField(verbose_name="管理员",max_length=11,)
    adminpwd=models.CharField(verbose_name='密码',max_length=64)

    def __str__(self):
        return self.adminname

class Task(models.Model):
    task=models.CharField(verbose_name="任务名",max_length=20)
    msg=models.TextField(verbose_name="任务描述")
    status_choice = ((1, "未完成"), (2, "已完成"),(3, "待完成"))
    status=models.SmallIntegerField(verbose_name="状态",choices=status_choice,default=1)
    depart=models.ForeignKey(verbose_name='部门',to='Department',to_field='id',on_delete=models.CASCADE,default=0)

class Order(models.Model):
    oid=models.CharField(verbose_name="订单号",max_length=64)
    title=models.CharField(verbose_name="名称",max_length=32)
    price=models.IntegerField(verbose_name="价格")

    status_choice = ((1, "待支付"),(2, "已支付"))
    status=models.SmallIntegerField(verbose_name="状态",choices=status_choice,default=1)
    admin=models.ForeignKey(verbose_name='管理员',to='Admins',to_field='id',on_delete=models.CASCADE,default=0)



