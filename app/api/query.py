from flask import request

from app.api import api
from app.utils.jsonp import JsonpFormat
from app.utils.query import Query
from app.utils.stulogin_manager import login_required


@api.route('/querySchedule', methods=['get'])
@login_required
def query_schedule(loginService):
    data = {'code': 0, 'msg': '查询成功!', 'data': {}}
    query = Query(loginService)
    grade = int(request.values.get('Grade', 0))
    term = int(request.values.get('term', 0))
    condition = None
    if grade > 0 and term > 0:
        condition = {'Grade': grade, 'term': term}
    data['data'] = query.query_schedule_a_term(condition)
    loginService.logout()
    return JsonpFormat.callback(data)


@api.route('/queryScore', methods=['get'])
@login_required
def query_score(loginService):
    data = {'code': 0, 'msg': '查询成功!', 'data': {}}
    query = Query(loginService)
    grade = int(request.values.get('Grade', 0))
    term = int(request.values.get('term', 0))
    data['data'] = query.query_score_a_term({'Grade': grade, 'term': term})
    from app.models.entry.score import Score
    data['data']['others'] = Score.calculate_all(data['data'])
    loginService.logout()
    return JsonpFormat.callback(data)


@api.route('/getCurrentWeek')
def get_current_week():
    from app import redis
    temp = redis.get('schooldays')
    weeks = -1
    if temp is not None:
        schooldays = float(temp.decode())
        import datetime
        current = datetime.datetime.now()
        t_schooldays = datetime.datetime.fromtimestamp(schooldays)
        days = (current - t_schooldays).days + t_schooldays.weekday()
        weeks = days // 7
        if days % 7 is not 0:
            weeks += 1
    return JsonpFormat.callback({'weeks': weeks, 'days': days})


@api.route('/getStuTimeLines')
@login_required
def get_stu_time_lines(loginService):
    data = {'code': 0, 'msg': '查询成功!', 'data': loginService.user.get_stu_time_line()}
    loginService.logout()
    return JsonpFormat.callback(data)
