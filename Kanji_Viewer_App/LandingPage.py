from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.button import MDRectangleFlatIconButton, MDRectangleFlatButton

# Utils
from utils import kill_screen

class StudyMethodPage(MDRelativeLayout):
    def __init__(self, master,**kwargs):
        super().__init__(**kwargs)
        self.master = master

        # Search Bar needs to be written in .kv lang

        self.btn_texts = ["List all kanji", "Load one kanji"]

        self.list_all_kanji_btn = MDRectangleFlatButton(text=self.btn_texts[0], pos_hint={"center_x": .5, "center_y": .6}, user_font_size="64sp", on_release=self.go_to_screen)
        self.single_kanji_study_btn = MDRectangleFlatButton(text=self.btn_texts[1], pos_hint={"center_x": .5, "center_y": .4}, user_font_size="64sp", on_release=self.go_to_screen)

class LandingPage(MDRelativeLayout):
    def __init__(self, master,**kwargs):
        super().__init__(**kwargs)
        self.master = master
        # self.size_hint = (None, None)
        self.btn_texts = ["AB Initio Kanji","      SL Kanji      ", "     HL Kanji      ", "HL Extra Kanji", "Kanji Koohii"]

        self.AB_initio_btn = MDRectangleFlatButton(text=self.btn_texts[0],  pos_hint={"center_x": .5, "center_y": .8}, user_font_size="64sp", on_release=self.go_to_screen)
        self.SL_btn = MDRectangleFlatButton(text=self.btn_texts[1],  pos_hint={"center_x": .5, "center_y": .6}, user_font_size="64sp", on_release=self.go_to_screen)
        self.HL_btn = MDRectangleFlatButton(text=self.btn_texts[2], pos_hint={"center_x": .5, "center_y": .4}, user_font_size="64sp", on_release=self.go_to_screen)
        self.HL_extra_btn = MDRectangleFlatButton(text=self.btn_texts[3], pos_hint={"center_x": .5, "center_y": .2}, user_font_size="64sp", on_release=self.go_to_screen)
        
        
        #self.Kanji_Koohi_btn = MDRectangleFlatButton(text=self.btn_texts[4], pos_hint={"center_x": .5, "center_y": .1}, user_font_size="64sp", on_release=self.go_to_koohii_screen)
        
        for btn in [self.AB_initio_btn, self.SL_btn, self.HL_btn,self.HL_extra_btn]:#, self.Kanji_Koohi_btn]: 
            self.add_widget(btn)

    def go_to_screen(self, inst):
        #self.master.screen_manager.current = "Landing Viewer"
        screen_name, self.master.kanji_level, level = "Kanji Viewer", inst.text.strip(), inst.text.strip()
        
        kill_screen("Kanji Viewer", lambda *args: self.master.create_kanji_page(self.master.kanji_level))
        """
        if self.master.screen_manager.has_screen(screen_name): 
            self.master.screen_manager.clear_widgets(screens=[self.master.screen_manager.get_screen(screen_name)])
        else: 
            self.master.create_kanji_page(level)
        self.master.screen_manager.current = screen_name
        """

    """
    def go_to_koohii_screen(self, inst):
        screen_name = "Kanji Koohii Viewer"
        if self.master.screen_manager.has_screen(screen_name): 
            self.master.screen_manager.clear_widgets(screens=[self.master.screen_manager.get_screen(screen_name)])
        else: 
            self.master.create_kanjikoohii_page()
        self.master.screen_manager.current = screen_name
    """

        