from app.models.entry.dataBase import DataBase


class Student(DataBase):

    def __init__(self, user):
        import base64
        data = base64.b64decode(user.encode()).decode()
        u = data.split('\n')
        self.yhm = u[0]
        self.mm = u[1]
        self.year = '20' + self.yhm[2:4]

    # 计算当前学年 int
    def get_current_school_year(self):
        import time
        tm = time.localtime(time.time())
        c = int(str(tm.tm_year)[-2:]) - int(self.yhm[2:4])
        return c if tm.tm_mon <= 9 else c + 1

    # 计算当前学期 int
    def get_current_term(self):
        import time
        tm = time.localtime(time.time()).tm_mon
        return 2 if 2 <= tm <= 7 else 1

    # 转变学年格式 str
    def turn_to_format_year(self, grade=1):
        if grade == 0:
            return ''
        return str(int(self.year) + grade - 1)

    # 获取学生阶段
    def get_stu_time_line(self):
        grades = [{'全部': 0}, {'大一': 1}, {'大二': 2}, {'大三': 3}, {'大四': 4}]
        terms = [{'全部': 0}, {'第一学期': 1}, {'第二学期': 2}]
        return {'Grades': grades[0:self.get_current_school_year()],
                'terms': terms,
                'current': {'Grade': self.get_current_school_year(),
                            'term': self.get_current_term()}}
