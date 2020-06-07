import json
from googletrans import Translator


class SettingsForTestCases:
    def __init__(self):
        try:
            with open('test_data.json', 'r', encoding='utf8') as json_file:
                self.test_dict = json.load(json_file)
        except Exception as error:
            print(error)

    def test_telegram_token(self):
        for data in self.test_dict:
            return data['test_telegram_api']

    def test_yandex_token(self):
        for data in self.test_dict:
            return data['test_yandex_api']

    def test_google_settings(self):
        for data in self.test_dict:
            service_urls = [data['google_settings'][0], data['google_settings'][1]]
            return service_urls


test_token_T = SettingsForTestCases().test_telegram_token()
test_token_Y = SettingsForTestCases().test_yandex_token()
test_data_G = Translator(SettingsForTestCases().test_google_settings())
