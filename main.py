import kivy
from kivy.properties import StringProperty
# from kivy.properties import NumericProperty
# from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
kivy.require('2.0.0')


class Task(BoxLayout):
    def __init__(self, **kwargs):
        super(Task, self).__init__(**kwargs)
        self.size_hint_y = 0.1
    pass


class TopPanelBar(BoxLayout):
    # ToggleButton
    pass


class TaskBar(StackLayout):
    pass


class MainWindows(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindows, self).__init__(**kwargs)

    my_text = StringProperty("ON")
    num = 0

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
