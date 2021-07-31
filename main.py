import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MainWindows(BoxLayout):
    def button_press(self):
        return "pressed"


class TestApp(App):
    def build(self):
        return MainWindows()


if __name__ == '__main__':
    TestApp().run()