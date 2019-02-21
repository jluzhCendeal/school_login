from app.models.entry.dataBase import DataBase


class Course(DataBase):
    # name = '课程名'
    # place = '课程地点'
    # typename = '类型'
    # teacher = '老师'
    # day = '星期几'
    # weeks_start_to_end = '第几周到第几周'
    # times_type = '0=all;1=单;2=双'
    # course_start_to_end = '第几节到第几节'
    # terms = '学年度'

    def __init__(self, json_data):
        try:
            self.name = json_data['kcmc']
            self.place = json_data['cdmc']
            self.typename = json_data['xsdm']
            self.teacher = json_data['xm']
            self.day = json_data['xqj']
            self.weeks_start_to_end = json_data['zcd'].split(',')
            self.class_start_to_end = json_data['jcs']
            self.terms = json_data['jxbmc']
        except Exception as e:
            print(e)
        self.times_type = []
        for w in self.weeks_start_to_end:
            if w.find('单') != -1:
                self.times_type.append(1)
            elif w.find('双') != -1:
                self.times_type.append(2)
            else:
                self.times_type.append(0)
