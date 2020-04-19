import kivy
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config

myApSize = {"width": '640', "height": '480'}

Config.set('graphics', 'width', myApSize['width'])
Config.set('graphics', 'width', myApSize['height'])

class TestApp(App):
    def build(self):
        fl = AnchorLayout(anchor_x='left', anchor_y='center')

        # fl.add_widget(Button(text="ОК", font_size=14, on_press=self.btn_press, background_color=[31, 1, 1, 7],
        #                      size_hint=(.5, .25),
        #                      pos=(int(myApSize['height'])/4, int(myApSize['width'])/8)))
        btn = Button(text='Count', size_hint=(.5, .25))
        fl.add_widget(btn)
        return fl


    def btn_press(self, instance):
        print("BUtton pressed")
        instance.text = "!!!"



if __name__ == '__main__':
    TestApp().run()