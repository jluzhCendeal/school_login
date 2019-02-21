import unittest

from app.models.entry.course import Course
from app.models.entry.student import Student
from app.utils.stulogin_manager import LoginService


class TestModels(unittest.TestCase):

    def setUp(self):
        self.loginService = LoginService()
        self.loginService.login('账号', '密码')

    def tearDown(self):
        self.loginService.logout()

    def test_student(self):
        d = '账号\n密码'
        import base64
        b_d = base64.b64encode(d.encode())
        stu = Student(b_d.decode())
        print(stu.get_current_school_year())
        self.assertEqual(0, stu.get_current_school_year())

    def test_course(self):
        data = self.loginService.get_schedule({'xnm': '2018', 'xqm': '3'})
        kbList = data['kbList']
        courseList = []
        count = len(kbList)
        if count > 0:
            for kc in kbList:
                c = Course(kc)
                courseList.append(c)
                print(c.get_json())

    def test_score(self):
        pass
