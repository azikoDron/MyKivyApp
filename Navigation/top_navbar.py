from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
Builder.load_file("KV/top_navbar.kv")


class TopNavBar(BoxLayout):

    def third_button_change_action(self):
        self.third_button.text = "Back"

    pass
