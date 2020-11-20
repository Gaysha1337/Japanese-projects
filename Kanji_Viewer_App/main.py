# -*- coding: utf-8 -*-
import os, json, plyer, sys, pathlib

from kivymd.app import MDApp
from kivy.properties import StringProperty, DictProperty

# Widgets
from kivymd.uix.button import MDIconButton, MDRectangleFlatButton, MDRectangleFlatIconButton
from kivymd.uix.toolbar import MDToolbar

# Screens and Screen-related
from kivy.uix.screenmanager import ScreenManager, Screen
from LandingPage import LandingPage
from KanjiViewer import KanjiViewer

# Utils
from kivy.config import Config
import kivy.resources

from kivy.core.text import LabelBase, DEFAULT_FONT
LabelBase.register(DEFAULT_FONT, 'NotoSansCJKjp-Regular.otf')

_USERAGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"

Config.set("network","useragent",_USERAGENT)

class ToolBar(MDToolbar):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.master = MDApp.get_running_app()
        self.title = MDApp.get_running_app().title
        self.id = "Toolbar"
        self.pos_hint = {"top":1}#{"center_y":.955}
        self.elevation = 10
        #self.left_action_items = [["cog", lambda x: MDApp.get_running_app().open_settings()]]
        
        self.right_action_items = [["home", lambda x: self.go_to_home_screen()]]
        if self.master.screen_manager.current == "Kanji Viewer":
            self.right_action_items.append(["autorenew", lambda x: self.load_new_kanji()])
        
        
    def go_to_home_screen(self):
        self.master.screen_manager.current = "Landing Page"

    def load_new_kanji(self):
        screen_name = "Kanji Viewer"
        self.master.screen_manager.clear_widgets(screens=[self.master.screen_manager.get_screen(screen_name)])
        self.master.create_kanji_page(self.master.kanji_level)
        self.master.screen_manager.current = screen_name

class GeneralScreen(Screen): 
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
           
    def on_pre_enter(self, *args, **kwargs):
        self.toolbar = ToolBar(title=MDApp.get_running_app().title, pos_hint={"top":1})#{"center_y":.955}
    
        #self.toolbar.right_action_items = [["home", lambda x: self.go_to_home_screen()] ]
        #if MDApp.get_running_app().screen_manager.current == "Kanji Viewer":
            #self.toolbar.right_action_items.append(["autorenew", lambda x: self.toolbar.load_new_kanji()])
        self.add_widget(self.toolbar) 

    def go_to_home_screen(self):
        #self.manager.current = "Search page"
        self.screen_manager.current = "Landing Page"


class IBKanjiReviewer(MDApp):
    kanji_level = StringProperty(None)
    def __init__(self):
        super().__init__()
        
    def build(self):
        self.title = "IB Kanji Reviewer"

        # Customizable Settings
        self.theme_cls.theme_style = "Dark" # Dark or Light
        self.theme_cls.primary_palette = "Pink"
        # Screen related
        self.screen_manager = ScreenManager()

        self.landing_page = LandingPage(self)
        screen = GeneralScreen(name="Landing Page")
        screen.add_widget(self.landing_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

    def create_kanji_page(self,level):
        self.page = KanjiViewer(self, level)
        screen = GeneralScreen(name="Kanji Viewer")
        screen.add_widget(self.page)
        self.screen_manager.add_widget(screen)

"""
# Needed for PyInstaller (Not apart of the root class)
def resourcePath():
    '''Returns path containing content - either locally or in pyinstaller tmp file'''
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS)

    return os.path.join(os.path.abspath("."))

"""
if __name__ == "__main__":
    #kivy.resources.resource_add_path(resourcePath()) # add this line
    IBKanjiReviewer().run()