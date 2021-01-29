from kivymd.app import MDApp
from kivymd.toast.kivytoast.kivytoast import toast

# Layouts
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.gridlayout import MDGridLayout

# Widgets
from kivymd.uix.button import MDFlatButton, MDIconButton, MDRaisedButton, MDRectangleFlatIconButton, MDRectangleFlatButton
from kivymd.uix.label import MDLabel, Label
from kivymd.uix.dialog import MDDialog
from kivy.uix.image import AsyncImage
from kivy.uix.carousel import Carousel
from kivy.uix.scrollview import ScrollView


# Utils
from utils import get_kanji_data, get_kanji_from_level, resource_path, kill_screen, switch_to_screen
from kivy.clock import Clock
from kivy.core.window import Window


class StrokeImage(AsyncImage):
    def __init__(self, source, width=200, height=200, **kwargs):
        super().__init__(**kwargs)
        self.source = source # Source is online
        self.allow_stretch=True
        self.keep_ratio=True
        self.pos_hint = {"center_x":.5, "center_y":.5}
        self.size_hint=(None,None)
        self.width=width
        self.height=height
        self.anim_delay = 0


class KanjiStrokeImageCarousel(Carousel):
    def __init__(self, imgs, **kwargs):
        super().__init__(**kwargs)
        self.imgs = imgs
        self.loop = True
        self.anim_type = "linear"#"in_back"

        for img in self.imgs:
            self.add_widget(StrokeImage(img))
        
        #Clock.schedule_interval(lambda *args:self.load_next(),2)
    
    
class KanjiViewer(ScrollView):
    def __init__(self, master, level,**kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        if self._keyboard.widget:
            # If it exists, this widget is a VKeyboard object which you can use to change the keyboard layout.
            pass
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        
        self.master = master
        self.level = level
        self.dialog = None

        self.effect_cls = "ScrollEffect"
        self.scroll_type = ["bars"]
        self.bar_width = "10dp"

        self.kanji_layout = MDRelativeLayout(adaptive_height=True)

        self.kanji_data =  get_kanji_from_level(self.level)

        if self.kanji_data is {} or self.kanji_data is None:
            toast("Error has occured; No internet connection; Site may be blocked")
            self.kanji_layout.add_widget(Label(text="Can't connect to the internet\nthe API may be blocked\nor poor connection", halign="center"))
        else:
            for k,v in self.kanji_data.items():
                setattr(self,k,v)

            self.btn_texts = ["     Show Meanings     ","       Show Radicals       ", "Show Example Words"]
            
            self.kanji_layout.add_widget(Label(text=str(self.kanji), font_size=75,halign="center", pos_hint={"center_y":.8}))
            self.kanji_layout.add_widget(Label(text=str(self.stroke_count), font_size=20,halign="center", pos_hint={"center_y":.7}))
            
            self.carousel = KanjiStrokeImageCarousel(self.stroke_order_images)
            #self.kanji_layout.add_widget(self.carousel)
            self.prev_btn = MDIconButton(icon="menu-left", user_font_size ="200sp", on_release = lambda x:self.carousel.load_previous(), pos_hint={"center_x":.1, "center_y":.5}) # pos_hint={"left":.2, "y":.5},
            self.next_btn = MDIconButton(icon="menu-right", user_font_size ="200sp", on_release = lambda x:self.carousel.load_next(), pos_hint={"center_x":.9, "center_y":.5}) # pos_hint={"right":.8, "y":.5}
            #self.kanji_layout.add_widget(self.prev_btn)
            #self.kanji_layout.add_widget(self.next_btn)
            print(self.kanji)

            for widget in [self.carousel, self.prev_btn, self.next_btn]:
                self.kanji_layout.add_widget(widget)

            for i, reading in enumerate(self.readings):
                self.kanji_layout.add_widget(Label(text=reading,font_size=20, pos_hint={"center_x":.5,"center_y":.3-(i/20)}))
            
            #print(self.radicals_data, "\n")
            #print(" ".join([j for j in [" ".join(i) for i in self.radicals_data]]))
            formated_radicals = " \n".join([rad for rad in [" :".join(tup) for tup in self.radicals_data]])

            formated_word_examples = "\n".join(self.example_words)

            #print(self.radicals_data, self.example_words, sep="\n")
            
            #self.kanji_layout.add_widget(Label(text=formated_radicals,halign="center", font_size=15, pos_hint={"center_x":.5,"center_y":.1}))
            self.meanings_btn = MDRaisedButton(text=self.btn_texts[0], pos_hint={"center_x":.1,"center_y":.15}, on_release=lambda x:self.showDialog("Meanings",self.meanings))
            self.kanji_layout.add_widget(self.meanings_btn)
            self.radicals_btn = MDRaisedButton(text=self.btn_texts[1], pos_hint={"center_x":.5,"center_y":.15}, on_release=lambda x:self.showDialog("Radicals",formated_radicals))
            self.kanji_layout.add_widget(self.radicals_btn)
            self.examples_btn = MDRaisedButton(text=self.btn_texts[2], pos_hint={"center_x":.9,"center_y":.15}, on_release=lambda x:self.showDialog("Example Words",formated_word_examples))
            self.kanji_layout.add_widget(self.examples_btn)
            self.add_widget(self.kanji_layout)


    def showDialog(self, title, text):
        self.dialog = None
        if not self.dialog:
            self.dialog = MDDialog(title=title,text=text,buttons=[MDFlatButton(text="CLOSE", on_release=lambda *args:self.dialog.dismiss())])
            self.dialog.open()

    def load_new_screen(self):
        current_screen = self.master.screen_manager.get_screen(self.master.screen_manager.current)
        current_screen.toolbar.load_new_kanji()

    # Keyboard methods
    def _keyboard_closed(self):
        #print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print('The key', keycode, 'have been pressed', ' - text is %r' % text, ' - modifiers are %r' % modifiers, sep="\n")
        if keycode[1] == "left" or keycode[1] == "a":
            self.carousel.load_previous()

        if keycode[1] in ["right","d"]:
            self.carousel.load_next()
        
        if keycode[1] == "enter" and not isinstance(self.dialog, MDDialog): 
            self.load_new_screen()
            #kill_screen("Kanji Viewer",self.master.create_kanji_page)
        
        if keycode[1] in ["escape","enter",27]:
            if isinstance(self.dialog, MDDialog):
                self.dialog.dismiss()

            
         # Load new kanji by pressing 'n'
        if keycode[1] == "n": self.load_new_screen()
            
        if keycode[1] == "m":
            if isinstance(self.dialog, MDDialog): self.dialog.dismiss()
            self.meanings_btn.trigger_action(0)
            
        if keycode[1] == "r":
            if isinstance(self.dialog, MDDialog): self.dialog.dismiss()
            self.radicals_btn.trigger_action(0)
        
        if keycode[1] == "e":
            if isinstance(self.dialog, MDDialog): self.dialog.dismiss()
            self.examples_btn.trigger_action(0)
        
        # Return True to accept the key. Otherwise, it will be used by the system.
        return True



            