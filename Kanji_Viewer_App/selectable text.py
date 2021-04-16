from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivymd.uix.textfield import MDTextField, TextfieldLabel
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.clock import Clock

from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.core.window import Window


class MyButton(TextfieldLabel):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        #self.source = 'atlas://data/images/defaulttheme/checkbox_off'
        self.pos_hint = {"center_x":.5, "center_y":.5}
        #self.size_hint = (.5,.09)
        #self.border
        self.text = "idk"
        #self.disabled = False
        #self.readonly = True
        #self.cursor_blink = False
        #self.mode = "rectangle"
        #self.multiline = False
        #Window.show_cursor = False
        self.font_size = "240sp"
        

    def on_touch_down(self, touch):
        #Clock.schedule_once(lambda dt: self.select_text())
        super().on_touch_down(touch)

    """
    def on_press(self):
        self.source = 'atlas://data/images/defaulttheme/checkbox_on'

    def on_release(self):
        self.source = 'atlas://data/images/defaulttheme/checkbox_off'
    """


class SampleApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark" # Dark or Light
        self.theme_cls.primary_palette = "Pink"
        screen = Screen(name="TEST")
        main_layout = MDRelativeLayout()
        main_layout.add_widget(MyButton())
        screen.add_widget(main_layout)
        return screen


SampleApp().run()