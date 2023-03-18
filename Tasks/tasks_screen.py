from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from Tasks.tasks_data import Tasks
from kivy.uix.screenmanager import Screen

Builder.load_file("KV/tasks_screen.kv")


class TasksWindow(Screen):
    my_text = StringProperty("ON")
    num = 0

    def __init__(self, **kwargs):
        super(TasksWindow, self).__init__(**kwargs)

    def toggle_method_def(self, *arg):
        if arg[0].state == "down":
            self.my_text = "OFF"
        else:
            self.my_text = "ON"
        # return True

    def ons(self, arg):
        if self.my_text == "ON":
            print(arg.state)
            self.num += 1
            arg.text = str(self.num)

    pass


class TasksBar(StackLayout):
    def __init__(self, **kwargs):
        super(TasksBar, self).__init__(**kwargs)
        # Adding task
        for task in Tasks.get_all_tasks():
            print(task)
            self.add_widget(Tasks(task[0], task[1], task[2], task[3]))

    pass
