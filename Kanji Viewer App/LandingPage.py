from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.button import MDRectangleFlatIconButton, MDRectangleFlatButton

class LandingPage(MDRelativeLayout):
    def __init__(self, master,**kwargs):
        super().__init__(**kwargs)
        self.master = master
        # self.size_hint = (None, None)
        # DO NOT DELETE THE SPACES IN "Read Manga"
        self.btn_texts = ["      SL Kanji      ", "     HL Kanji      ", "HL Extra Kanji"]

        self.SL_btn = MDRectangleFlatButton(text=self.btn_texts[0],  pos_hint={"center_x": .5, "center_y": .8}, user_font_size="64sp", on_release=self.go_to_screen)
        self.HL_btn = MDRectangleFlatButton(text=self.btn_texts[1], pos_hint={"center_x": .5, "center_y": .6}, user_font_size="64sp", on_release=self.go_to_screen)
        self.HL_extra_btn = MDRectangleFlatButton(text=self.btn_texts[2], pos_hint={"center_x": .5, "center_y": .4}, user_font_size="64sp", on_release=self.go_to_screen)
        self.add_widget(self.SL_btn)
        self.add_widget(self.HL_btn)
        self.add_widget(self.HL_extra_btn)

    def go_to_screen(self, inst):
        #self.master.screen_manager.current = "Landing Viewer"
        screen_name = "Kanji Viewer"
        self.master.kanji_level = inst.text.strip()
        if not self.master.screen_manager.has_screen(screen_name):
            self.master.create_kanji_page(inst.text)
        else:
            self.master.screen_manager.clear_widgets(screens=[self.master.screen_manager.get_screen(screen_name)])
            self.master.create_kanji_page(inst.text)
        
        print(self.master.kanji_level, "in landing page meth mas k l")
        self.master.screen_manager.current = screen_name
        