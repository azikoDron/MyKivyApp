from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from baseSdk import SaveData


class Task(BoxLayout):
    TASK_SIZE = 0.1
    task_id = NumericProperty(0)
    task_name = StringProperty('Null')
    task_subject = StringProperty('Null')
    task_des = StringProperty('Null')

    def __init__(self, task_id, task_name, task_subject, task_des=None,  **kwargs):
        super(Task, self).__init__(**kwargs)
        self.task_id = task_id
        self.size_hint_y = Task.TASK_SIZE
        self.task_name = task_name
        self.task_subject = task_subject
        self.task_des = task_des

    # Change methods below, by send data API.
    def save_task(self):
        self.task_id = SaveData().save_task_data(self.task_name, self.task_subject,
                                                 self.task_des)
        return True

    @staticmethod
    def get_task_by_id(str_id):
        return SaveData().get_task_by_id(str(str_id))

    @staticmethod
    def get_all_tasks():
        return SaveData().get_all_tasks()
