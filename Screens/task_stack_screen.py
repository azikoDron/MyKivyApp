from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.stacklayout import StackLayout
from Tasks.tasks_data import Tasks
from Navigation.top_navbar import TopNavBar
Builder.load_file("KV/tasks_stack_screen.kv")


class TasksStackScreen(Screen):
    # def __init__(self, **kwargs):
    #     super(TasksWindow, self).__init__(**kwargs)
    #     self.add_widget()
    pass


class TasksBar(StackLayout):
    def __init__(self, **kwargs):
        super(TasksBar, self).__init__(**kwargs)
        # Adding task
        for task in Tasks.get_all_tasks():
            # print(task)
            self.add_widget(Tasks(task[0], task[1], task[2], task[3]))

    pass
