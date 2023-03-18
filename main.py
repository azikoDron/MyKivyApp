import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from Tasks.tasks_screen import TasksWindow
from Tasks.create_task import CreateTask


kivy.require('2.0.0')


class TopPanelBar(Screen):
    pass


class StickerApp(App):
    def build(self):
        sc_m = ScreenManager()
        sc_m.add_widget(TasksWindow(name="tasks_window"))
        sc_m.add_widget(CreateTask(name="create_task"))
        return sc_m


if __name__ == '__main__':
    StickerApp().run()
