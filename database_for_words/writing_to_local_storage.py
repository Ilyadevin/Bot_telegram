import json


class ToJson:
    def __init__(self, test_data):
        self.data_to_json = test_data

    def creating_points_in_json(self):
        with open('db_json.json', 'a', 'utf8') as json_file:
            json.dump(self.data_to_json, json_file)
