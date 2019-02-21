from app.models.entry.course import Course
from app.models.entry.score import Score


class Query:
    terms = {0: '', 1: '3', 2: '12'}

    def __init__(self, login_service):
        self.loginService = login_service
        if login_service.user is None:
            raise Exception('LoginService user is not None')

    # 查询某一学期分数
    # 参数 {‘Grade':年级,'term':学期}
    # 返回{total:总数，list:列表}
    def query_score_a_term(self, condition={'Grade': 0, 'term': 0}):
        data = {'total': 0, 'list': []}
        grade = condition['Grade']
        term = condition['term']
        current_term = self.loginService.user.get_current_school_year()
        arg = {
            'xnm': '',
            'xqm': '',
            'queryModel.showCount': '5000'
        }
        if 0 <= grade <= current_term and 0 <= term < 3:
            arg['xnm'] = self.loginService.user.turn_to_format_year(grade)
            arg['xqm'] = self.terms[term]
            scores = self.loginService.get_sore(arg)
            ls = Score.create_scores_from_json(scores)
            data['total'] = len(ls)
            data['list'] = ls
        return data

    # 查询某一学年的课表
    # 参数 {‘Grade':年级,'term':学期}
    # 返回{total:总数，list:列表}
    def query_schedule_a_term(self, condition=None):
        data = {'total': 0, 'list': []}
        current_term = self.loginService.user.get_current_school_year()
        grade = current_term
        term = self.loginService.user.get_current_term()
        if condition is not None:
            grade = condition['Grade']
            term = condition['term']
        if 1 <= grade <= current_term and 0 < term < 3:
            arg = {
                'xnm': self.loginService.user.turn_to_format_year(grade),
                'xqm': self.terms[term]
            }
            source = self.loginService.get_schedule(arg)
            kbList = source['kbList']
            courseList = []
            count = len(kbList)
            data['total'] = count
            if count > 0:
                for kc in kbList:
                    c = Course(kc)
                    courseList.append(c.get_json())
                data['list'] = courseList
        return data
