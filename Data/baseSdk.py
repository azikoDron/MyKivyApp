import sqlite3
import os

'''
SQL SAVE Variant ...

'''


class SaveData:
    def __init__(self, db_name='template', dp_location='./Data'):
        self.db_name = db_name
        self.dp_location = dp_location + str(os.sep) + db_name
        self.db_connection = self.db_connection()
        try:
            self.db_cursor('create table task(id number, task_name varchar2, task_subject varchar2, task_des varchar2)')
        except sqlite3.OperationalError:
            pass

    def save_task_data(self, task_name, task_subject, task_des="Null"):
        task_id = [i for i in self.db_cursor("select max(id) from task")]
        print(task_id[0], task_id)
        self.db_cursor(f"insert into task values('{int(task_id[0][0])+1}','{task_name}','{task_subject}','{task_des}')")
        self.db_cursor('commit')
        return task_id

    def get_all_tasks(self):
        return self.db_cursor('select * from task where id > 0 ')

    def get_task_by_id(self, str_id):
        return self.db_cursor(f'select * from task where id = {str_id}')

    def db_connection(self):
        return sqlite3.connect(self.dp_location)

    def db_cursor(self, script):
        return self.db_connection.cursor().execute(script)
