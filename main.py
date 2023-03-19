import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from Screens.task_create_screen import TaskCreateScreen
from Navigation.top_navbar import TopNavBar
from Screens.main_screen import MainScreenView
from Screens.task_stack_screen import TasksStackScreen

# from Tasks.tasks_screen import TasksWindow

kivy.require('2.0.0')


class StickerApp(App):
    def build(self):
        sc_m = ScreenManager()
        sc_m.add_widget(MainScreenView(name="main_screen"))
        sc_m.add_widget(TasksStackScreen(name="task_stack_window"))

        return sc_m


if __name__ == '__main__':
    StickerApp().run()
