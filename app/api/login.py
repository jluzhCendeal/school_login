import base64
from flask import request, make_response

from app.utils.jsonp import JsonpFormat
from . import api


@api.route('/login', methods=['post', 'get'])
def login():
    yhm = request.values.get('yhm')
    mm = request.values.get('mm')
    token = request.values.get('token')
    data = {'msg': '未登录！', 'code': '-1', 'data': {}}
    if (yhm is None or mm is None) and token is not None:
        from app.models.entry.student import Student
        user = Student(token)
        yhm = user.yhm
        mm = user.mm

    from app.utils.stulogin_manager import LoginService
    loginService = LoginService()
    flag = loginService.login(yhm, mm)
    if flag:
        data['code'] = 0
        data['msg'] = '已登录！'
        user = base64.b64encode((yhm + '\n' + mm).encode()).decode()
        data['data'] = {'token': user}
        resp = make_response(JsonpFormat.callback(data))
        resp.set_cookie('token', user)
        loginService.logout()
        return resp

    return JsonpFormat.callback(data)
