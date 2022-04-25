"""djbiliproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from apptest import views
from django.conf import settings
from django.urls import path,re_path
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$',serve,{'docume_root':settings.MEDIA_ROOT},name='media'),
    path('admin/', views.adminsth),
    path('news/', views.newwatch),
    path('login/', views.login),
    path('info_list/',views.info_list),
    path('info_list/add/', views.info_add),
    path('info_list/delete/', views.info_delete),
    #部门
    path('depart_info/', views.depart_info),
    path('depart_info/add/', views.depart_infoadd),
    path('depart_info/del/', views.depart_infodel),
    path('depart_info/<int:nid>/edit/', views.depart_infoedit),
    path('depart_info/mult/', views.depart_infomult),

     #用户
    path('users_info/', views.users_info),
    path('users_info/add/', views.users_infoadd),
    path('users_info/<int:nid>/edit/', views.users_infoedit),
    path('users_info/del/', views.users_infodel),
    #靓号
    path('phones_info/', views.phones_info),
    path('phones_info/add/', views.phones_infoadd),
    path('phones_info/<int:nid>/edit/', views.phones_infoedit),
    path('phones_info/del/', views.phones_infodel),
    #管理员
    path('admins_info/', views.admins_info),
    path('admins_info/add/', views.admins_infoadd),
    path('admins_info/<int:nid>/edit/', views.admins_infoedit),
    path('admins_info/del/', views.admins_infodel),
    path('admins_info/<int:nid>/reset/', views.admins_inforeset),
    #登录
    path('to_login/', views.to_login),
    path('to_logout/', views.to_logout),

    #任务
    path('task_info/', views.task_info),
    path('task_info/add/', views.task_infoadd),

    #订单
    path('order_info/', views.order_info),
    path('order_info/add/', views.order_infoadd),
    path('order_info/delete/', views.order_infodelete),
    path('order_info/detail/', views.order_infodetail),
    path('order_info/edit/', views.order_infoedit),

    #数据统计
    path('echarts_info/', views.echarts_info),
    path('echarts_info/bar', views.echarts_infobar),

    #上传文件
    path('upload_info/', views.upload_info),
    path('upload_form/', views.upload_form),



]
