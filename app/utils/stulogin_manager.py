import json
from functools import wraps
import requests


class LoginService:
    __host__ = 'http://125.89.69.234'

    def __init__(self):
        self.session = requests.Session()
        self.user = None

    # 模拟登陆
    def login(self, yhm, mm):
        url = self.__host__ + '/xtgl/login_slogin.html'
        data = {'yhm': yhm, 'mm': mm}
        content = self.session.post(url, data)
        headers = content.headers
        if 'Set-Cookie' not in headers:
            print("已登陆：[{}]".format(headers.values()))
            return True
        print('登陆失败:[{}]'.format(headers.values()))
        return False

    def login_user(self, user):
        flag = self.login(user.yhm, user.mm)
        if flag:
            self.user = user
        return flag

    # 注销
    def logout(self):
        url = self.__host__ + '/logout'
        content = self.session.get(url)
        if content.status_code == 200:
            print('已登出!')
            return True
        print('操作异常!')
        return False

    # 查询学分
    def get_sore(self, condition):
        url = self.__host__ + '/cjcx/cjcx_cxDgXscj.html?doType=query&gnmkdm=N305005'
        content = self.session.post(url, data=condition)
        data = json.loads(content.text)
        return data

    # 查询课表
    def get_schedule(self, condition):
        url = self.__host__ + '/kbcx/xskbcx_cxXsKb.html?gnmkdm=N253508'
        content = self.session.post(url, data=condition)
        data = json.loads(content.text)
        return data


def login_required(next_func):
    @wraps(next_func)
    def decorated(*args, **kwargs):
        loginService = LoginService()
        from flask import request
        temp = request.cookies.get('token')
        if temp is not None:
            from app.models.entry.student import Student
            user = Student(temp)
            if loginService.login_user(user):
                return next_func(loginService, *args, **kwargs)
        from app.utils.jsonp import JsonpFormat
        return JsonpFormat.callback({'code': '-1', 'msg': '未登录!'})
    return decorated
