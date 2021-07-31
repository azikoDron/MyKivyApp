import kivy
from kivy.properties import StringProperty

kivy.require('2.0.0')
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MainWindows(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindows, self).__init__(**kwargs)
    # self.my_text = "U!"
    my_text = StringProperty("1")

    def ons(self):
        self.my_text = "0"
        print('Pressed')

    pass


class TestApp(App):
    def build(self):
        return MainWindows()


if __name__ == '__main__':
    TestApp().run()