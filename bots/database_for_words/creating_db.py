import psycopg2
connection = psycopg2.connect(database='main_database',
            user='helper_io',
            password=f'{}',
            host='127.0.0.1',
            port='5432',
            )
cursor=connection.cursor()
def creating_local():
    try:
        cursor.execute('''CREATE TABLE USERS
        (ID SERIAL PRIMARY KEY NOT NULL,
        USER_NAME TEXT NOT NULL
        WORDS_TO_TRANSLATE TEXT NOT NULL
        TRANSLATED_WORDS TEXT NOT NULL)'''
        )
    except Exception as error:
        print('There is an exception, database already excits!')