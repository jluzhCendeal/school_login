from app.models.entry.dataBase import DataBase


class Score(DataBase):

    def __init__(self, json_data):
        try:
            self.id = json_data['kch_id']
            self.name = json_data['kcmc']
            self.type = json_data['kcxzdm']
            self.credit = json_data['xf']
            self.percentile = json_data['bfzcj']
            self.score = json_data['cj']
            self.gpa = json_data['jd']
            self.teacher = json_data['jsxm']
            self.school_year = json_data['xnm']
            self.term_id = json_data['xqm']
        except Exception as e:
            print(e)

    @staticmethod
    def create_scores_from_json(obj):
        scores = []
        for cj in obj['items']:
            score = Score(cj)
            scores.append(score.get_json())
        return scores

    @staticmethod
    def calculate_all(source_list):
        data = {'per_gpa': 0,
                'per_percentile': 0,
                'total_credit': 0,
                'required_credit': 0,
                'selected_major_credit': 0,
                'public_credit': 0,
                'effective_total': 0
                }
        total = source_list['total']
        gpa = 0
        percentile = 0
        for i in source_list['list']:
            gpa += float(i['gpa'])
            percentile += int(i['percentile'])

            data['total_credit'] += float(i['credit'])
            if i['percentile'] >= 60:
                data['effective_total'] += 1
                if i['type'] == '06':
                    data['public_credit'] += float(i['credit'])
                elif i['type'] == '01':
                    data['required_credit'] += float(i['credit'])
                elif i['type'] == '03':
                    data['selected_major_credit'] += float(i['credit'])
        if total is not 0:
            data['per_percentile'] = percentile // total
            data['per_gpa'] = round(gpa / total, 2)
        return data
