from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class Auth(MiddlewareMixin):
    def process_request(self,request):
        #排除非登录状态可访问页面
        nosessionurl=['/to_login/']
        if request.path_info == "/to_login/":
            return
        #读取当前用户session信息
        info_dict=request.session.get('uid',1)
        if info_dict:
            return
        return redirect('/to_login/')

    # def process_response(self,request,response):
    #     return
