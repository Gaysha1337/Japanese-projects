# -*- coding: utf-8 -*-
import os, json, plyer, sys, pathlib

from kivy.config import Config

_USERAGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
Config.set("network","useragent",_USERAGENT)

from kivymd.app import MDApp
from kivy.properties import StringProperty, DictProperty

# Widgets
from kivymd.uix.button import MDIconButton, MDRectangleFlatButton, MDRectangleFlatIconButton
from kivymd.uix.toolbar import MDToolbar

# Screens and Screen-related
from KanjiScreen import GeneralScreen
from kivy.uix.screenmanager import ScreenManager, Screen
from LandingPage import LandingPage#, LevelSelectionPage
from KanjiViewer import KanjiViewer
#from KanjiKoohiiViewer import KanjiKoohiiViewer

# Utils
from utils import resource_path, create_screen
from kivy.resources import resource_add_path
from KanjiKoohiiAPI import stories_csv_to_json


from kivy.core.text import LabelBase, DEFAULT_FONT
LabelBase.register(DEFAULT_FONT, resource_path('DATA/NotoSansCJKjp-Regular.otf'))




class IBKanjiReviewer(MDApp):
    kanji_level = StringProperty(None)
    def __init__(self):
        super().__init__()
        
    def build(self):
        self.title = "IB Kanji Reviewer"
        self.icon = resource_path("web_hi_res_512.ico")

        self.kanji_koohi_stories_list = stories_csv_to_json()

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

    # Creates the page where kanji are displayed (stroke order + count, radicals, examples words, meanings)
    def create_kanji_page(self,level):
        self.page = KanjiViewer(self, level)
        create_screen("Kanji Viewer", self.page)
        """
        screen = GeneralScreen(name="Kanji Viewer")
        screen.add_widget(self.page)
        self.screen_manager.add_widget(screen)
        """

    # Creates the page where kanji are displayed (stroke order + count, radicals, examples words, meanings)
    """
    def create_kanjikoohii_page(self):
        self.page = KanjiKoohiiViewer(self)
        screen = GeneralScreen(name="Kanji Koohii Viewer")
        screen.add_widget(self.page)
        self.screen_manager.add_widget(screen)
    """

if __name__ == "__main__":
    #kivy.resources.resource_add_path(resourcePath()) # add this line
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    
    # https://stackoverflow.com/questions/64142867/kivymd-with-pyinstaller-hooks-images-not-showing-in-the-standalone-exe
    if getattr(sys, 'frozen', False):
        # this is a Pyinstaller bundle
        resource_add_path(sys._MEIPASS)
        resource_add_path(os.path.join(sys._MEIPASS, 'DATA'))
    IBKanjiReviewer().run()
