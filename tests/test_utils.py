import unittest

from app.utils.query import Query
from app.utils.stulogin_manager import LoginService


class TestUnit(unittest.TestCase):
    def testStu(self):

        loginService = LoginService()
        self.assertTrue(loginService.login("账号", "密码"))
        print(loginService.get_sore({'queryModel.showCount': '5000'}))
        self.assertTrue(loginService.logout())

    def test_query(self):
        from app.models.entry.student import Student
        d = '用户账号\n用户密码'
        import base64
        b_d = base64.b64encode(d.encode())
        stu = Student(b_d.decode())

        loginService = LoginService()
        if loginService.login_user(stu):
            q = Query(loginService)
            ls = q.query_schedule_a_term()
            print(ls)
