from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, ObjectProperty
Builder.load_file("KV/top_navbar.kv")


class TopNavBar(BoxLayout):

    button_name = StringProperty("Create")
    # third_button = ObjectProperty()

    def third_button_change_action(self):
        if self.parent.parent.manager.current == "task_stack_screen":
            self.button_name = "Create"
            self.parent.parent.manager.current = "main_screen"
        elif self.parent.parent.manager.current == "main_screen":
            self.button_name = "Back"
            self.parent.parent.manager.current = "task_stack_screen"
    pass


class LeftNavBar(FloatLayout):
    pass