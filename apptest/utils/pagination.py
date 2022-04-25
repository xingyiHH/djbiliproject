#自定义页码组件
import copy
from django import forms
from django.utils.safestring import mark_safe


class Pagination(forms.ModelForm):
    def __init__(self,request,queryset,page_size=10,page_param="page",plus=5):
        """
        :param request: 请求对象
        :param queryset: 数据
        :param page_size: 每页展示数据条数
        :param page_param: url请求param
        :param plus: 页码展示当前前后plus页
        """
        query_dict=copy.deepcopy(request.GET)
        query_dict.mutable=True  #解决？xx=&Xyy=  url拼接问题
        self.query_dict=query_dict
        self.page_param=page_param

        page=request.GET.get( self.page_param, '1')
        if page.isdecimal():
            page =int(page)
        else:
            page=1

        self.page=page
        self.page_size=page_size
        self.start=(self.page-1)*page_size
        self.end = page * page_size
        self.page_queryset=queryset[self.start:self.end]  #分页列表展示
        self.plus=plus

        total_count=queryset.count()
        pages_sum,div=divmod(total_count,page_size)
        if div>1:
            self.pages_sum=pages_sum + 1
            print(self.pages_sum)
        self.pages_sum=pages_sum+1


    def html(self):
        # 计算当前页的前后5页面
        self.plus = 5
        if self.pages_sum > 2 * self.plus + 1:
            if self.page <= self.plus:
                self.start_page = 1
                self.end_page = 2 * self.plus + 1
            else:
                if (self.page + self.plus) > self.pages_sum:
                    self.start_page = self.pages_sum - 2 * self.plus
                    self.end_page = self.pages_sum
                else:
                    self.start_page = self.page - self.plus
                    self.end_page = self.page + self.plus
        else:
            self.start_page = 1
            self.end_page = self.pages_sum

        page_ele_list = []

        # 上一页
        if self.page == 1:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        page_ele_list.append(prev)

        # 页面
        for i in range(self.start_page, self.end_page + 1):
            if i == self.page:
                self.query_dict.setlist(self.page_param, [i])
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                self.query_dict.setlist(self.page_param, [i])
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_ele_list.append(ele)

        # 下一页
        if self.page < self.pages_sum:
            self.query_dict.setlist(self.page_param,[self.page + 1])
            nextp = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())

        else:
            self.query_dict.setlist(self.page_param,[self.pages_sum])
            nextp = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        page_ele_list.append(nextp)

        page_string = mark_safe("".join(page_ele_list))
        return page_string

