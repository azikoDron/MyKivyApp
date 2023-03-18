from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from Data.baseSdk import SaveData
from kivy.lang import Builder
Builder.load_file("KV/create_task.kv")


class CreateTask(Screen, BoxLayout):
    pass