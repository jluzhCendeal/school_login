class DataBase:
    def get_json(self):

        items = vars(self).items()
        data = {}
        for k, v in items:
            data[k] = v
        return data
