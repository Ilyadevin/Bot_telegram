import psycopg2
import json
import time
class DataBase:
    def __init__(self,):
        self.db_status = 0
        with open('settings_for_db.json', 'r', encoding='utf8') as json_file:
            time.sleep(1)
            self.reader = json.load(json_file)
    def connection_settings(self):
        connection = psycopg2.connect(database='main_database',
                    user='helper_io',
                    password=f'{}',
                    host='127.0.0.1',
                    port='5432',
                    )
        self.cursor = connection.cursor()
    def creating_local(self):
        if self.db_status == 0:
            try:
                self.cursor.execute('''CREATE TABLE USERS
                (ID SERIAL PRIMARY KEY NOT NULL,
                USER_NAME TEXT NOT NULL
                WORDS_TO_TRANSLATE TEXT NOT NULL
                TRANSLATED_WORDS TEXT NOT NULL)'''
                )
                self.db_status = 1
            except Exception as error:
                print('There is an exception, database already excits!/n
                        f'{error}'
                    )
        else:
            return Exception