import json


class JsonpFormat:
    name = 'jsonpCallback'

    @classmethod
    def callback(cls, data_json):
        return "{}({});".format(JsonpFormat.name, json.dumps(data_json))
