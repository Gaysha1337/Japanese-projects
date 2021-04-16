from utils import kill_screen
from kivymd.app import MDApp

from kivy.uix.screenmanager import Screen

from kivymd.uix.toolbar import MDToolbar


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
        kill_screen("Kanji Viewer", lambda *arg: self.master.create_kanji_page(self.master.kanji_level))
        """
        screen_name = "Kanji Viewer"
        self.master.screen_manager.clear_widgets(screens=[self.master.screen_manager.get_screen(screen_name)])
        self.master.create_kanji_page(self.master.kanji_level)
        self.master.screen_manager.current = screen_name
        """

class GeneralScreen(Screen): 
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
           
    def on_pre_enter(self, *args, **kwargs):
        self.toolbar = ToolBar()
        self.add_widget(self.toolbar) 

    def go_to_home_screen(self):
        #self.manager.current = "Search page"
        self.screen_manager.current = "Landing Page"