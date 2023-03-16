import kivy
from kivy.properties import StringProperty
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from task import Task
kivy.require('2.0.0')


class TopPanelBar(BoxLayout):
    pass


class TaskBar(StackLayout):
    def __init__(self, **kwargs):
        super(TaskBar, self).__init__(**kwargs)
        # Adding task
        for task in Task.get_all_tasks():
            print(task)
            self.add_widget(Task(task[0], task[1], task[2], task[3]))

    pass


class MainWindows(BoxLayout):
    my_text = StringProperty("ON")
    num = 0

    def __init__(self, **kwargs):
        super(MainWindows, self).__init__(**kwargs)

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


class TestApp(App):
    def build(self):
        return MainWindows()


if __name__ == '__main__':
    TestApp().run()
