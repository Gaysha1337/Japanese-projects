from kivymd.app import MDApp
from kivymd.toast.kivytoast.kivytoast import toast
from kivymd.uix.boxlayout import MDBoxLayout

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
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import OneLineListItem

# Utils
from utils import get_kanji_data, get_kanji_from_level, resource_path, kill_screen, switch_to_screen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import platform


class StrokeImage(AsyncImage):
    def __init__(self, source, width=250, height=250, **kwargs):
        super().__init__(**kwargs)
        self.source = source # Source is online
        self.allow_stretch=True
        self.keep_ratio=True
        self.pos_hint = {"center_x":.5, "center_y":.6}
        self.size_hint=(None,None)
        self.width=width
        self.height=height
        self.anim_delay = 0
        


class KanjiStrokeImageCarousel(Carousel):
    def __init__(self, imgs, **kwargs):
        super().__init__(**kwargs)
        self.master = MDApp.get_running_app()
        self.imgs = imgs
        self.loop = True
        self.anim_type = "linear"#"in_back"
        self.size_hint = (1, .5)
        self.pos_hint = {"center_y":.6}

        for img in self.imgs: self.add_widget(StrokeImage(img))
        
        #Clock.schedule_interval(lambda *args:self.load_next(),2)
    """
    def on_touch_down(self, touch):
        if touch.is_double_tap:
            print(touch)
            print("-"*15)
            for child in self.walk():
                if self.collide_widget(child) and isinstance(child, HighlightableText):
                    print(child, "coll with ef")
                    child.select_all()

            print("-"*15, "\n")


    def on_touch_move(self, touch):
        #return super().on_touch_move(touch)
        print(touch, touch.grab_current,touch.__dict__, sep="\n")
        for child in self.walk():
            if self.collide_widget(child) and isinstance(child, (HighlightableText)):
                print(child, "coll with ef")
    """
    
    
class HighlightableText(MDTextField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.master = MDApp.get_running_app()
        self.multiline = True
        self.readonly = True
        self.cursor_blink = False
        self.cursor_color = (0,0,0,0)
        self.active_line = False
        self.line_color_normal = (0,0,0,0)
        self.halign = "center"
        self.mode = "line"
        #self.pos_hint = {"center_x":.5, "center_y":.5}
        #self.size_hint_x = 0.11 * len(self._lines) + 0.1
        #self.size_hint = (0.11 * len(self._lines) + 0.1, None)
        self.allow_copy = True
        #self.disabled = True
        self.bind(text=self.text_changed)
        #self.parent.width = max([line.width for line in self._lines_labels])
    def text_changed(self, text_input, text):
        if len(text) > 0:
            #text_input.size_hint_x = None
            # text_input.width = text_input._lines_labels[0].width + 5
            for line in text_input._lines_labels:
                text_input.parent.width += line.width + 5        
    """
    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            self.select_all()      
            #self.select_text(self.cursor_offset(), self.cursor_index())
            #print(self.cursor_offset())
            
        return super().on_touch_move(touch)
    """
    """
    def on_text(self, *args, **kwargs):
        pass
    """
    """
    def on_focus(self, *args):
        #print("higlight text focus: ", self.focus, self.text)
        if self._selection_finished and self.selection_text == "":
            #self.focus = False
            print("in on_focus meth, if not focus: -->","higlight text focus: ", self.focus, self.selection_text)
        super().on_focus(*args)
    """
            
    def on_selection_text(self, instance, value):
        super().on_selection_text(instance, value)
        self.delete_selection()
        if value == "":
            print("Blank", value)
            self.focus = False
            self.cancel_selection()
        

class DialogContent(MDBoxLayout):
    def __init__(self, *args,**kwargs):
        #self.adaptive_size = True
        super().__init__(*args, **kwargs)

"""    
class InfoDialog(MDDialog):
    def __init__(self,title, text,*args,**kwargs):
        
        self.type = "custom"
        self.title = title
        self.text = text
        #self.content_cls = DialogContent()
        
        self.buttons = [MDFlatButton(text="CLOSE", on_release =self.dismiss)]
        
        #self.create_items()
        super().__init__(*args,**kwargs)
        self.content_cls = DialogContent()
        
        #self.add_widget(HighlightableText("text"))
"""

class KanjiViewer(ScrollView):
    def __init__(self, master, level,**kwargs):
        super().__init__(**kwargs)
        
        if platform != "android":
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
        self.pos_hint = {"top":.9}

        self.kanji_layout = MDRelativeLayout()

        self.kanji_data =  get_kanji_from_level(self.level)

        if self.kanji_data is {} or self.kanji_data is None:
            toast("Error has occured; No internet connection; Site may be blocked")
            self.kanji_layout.add_widget(Label(text="Can't connect to the internet\nthe API may be blocked\nor poor connection", halign="center"))
        else:
            for k,v in self.kanji_data.items():
                setattr(self,k,v)

            self.btn_texts = ["     Show Meanings     ","       Show Radicals       ", "Show Example Words"]
            
            #self.kanji_layout.add_widget(Label(text=str(self.kanji), font_size=75,halign="center", pos_hint={"center_y":.8}))
            #self.kanji_layout.add_widget(Label(text=str(self.stroke_count), font_size=20,halign="center", pos_hint={"center_y":.7}))
            

            self.kanji_layout.add_widget(
                HighlightableText(text=f"{str(self.kanji)}: {self.stroke_count}", font_size="40sp", pos_hint={"center_x":.5,"center_y":.9})
            )
            self.carousel = KanjiStrokeImageCarousel(self.stroke_order_images)
            self.kanji_layout.add_widget(self.carousel)

            if platform != "Android":
                self.prev_btn = MDIconButton(icon="menu-left", user_font_size ="200sp", on_release = lambda x:self.carousel.load_previous(), pos_hint={"center_x":.1, "center_y":.6}) # pos_hint={"left":.2, "y":.5},
                self.next_btn = MDIconButton(icon="menu-right", user_font_size ="200sp", on_release = lambda x:self.carousel.load_next(), pos_hint={"center_x":.9, "center_y":.6}) # pos_hint={"right":.8, "y":.5}
                self.kanji_layout.add_widget(self.prev_btn)
                self.kanji_layout.add_widget(self.next_btn)
            
            


            """
            for i, reading in enumerate(self.readings):
                # HighlightableText(text=reading, font_size=20, pos_hint={"center_x":.5,"center_y":.3-(i/20)})
                self.kanji_layout.add_widget(
                    HighlightableText(text=reading, font_size=20, pos_hint={"center_x":.4,"center_y":.3-(i/30)})
                )
            """
            self.readings_formatted = "\n".join([f"{k}: {v}" for k,v in self.readings.items()])
            self.kanji_layout.add_widget(
                HighlightableText(text=f"{self.readings_formatted}", font_size="20sp", pos_hint={"center_x":.5,"center_y":.35})
            )

            #print(" ".join([j for j in [" ".join(i) for i in self.radicals_data]]))
            formated_radicals = " \n".join([rad for rad in [" :".join(tup) for tup in self.radicals_data]])

            formated_word_examples = "\n".join(self.example_words)
            
            #self.kanji_layout.add_widget(Label(text=formated_radicals,halign="center", font_size=15, pos_hint={"center_x":.5,"center_y":.1}))
            self.meanings_btn = MDRaisedButton(text=self.btn_texts[0], pos_hint={"center_x":.1,"center_y":.2}, on_release=lambda x:self.showDialog("Meanings",self.meanings))
            
            self.radicals_btn = MDRaisedButton(text=self.btn_texts[1], pos_hint={"center_x":.5,"center_y":.2}, on_release=lambda x:self.showDialog("Radicals",formated_radicals))
            #self.kanji_layout.add_widget(self.radicals_btn)
            self.examples_btn = MDRaisedButton(text=self.btn_texts[2], pos_hint={"center_x":.9,"center_y":.2}, on_release=lambda x:self.showDialog("Example Words",formated_word_examples))
            #self.kanji_layout.add_widget(self.examples_btn)
            
            for btn in [self.meanings_btn, self.radicals_btn, self.examples_btn]:
                self.kanji_layout.add_widget(btn)
            self.add_widget(self.kanji_layout)


    def showDialog(self, title, text):
        self.dialog = None
        if not self.dialog:
            #self.dialog = MDDialog(title=title,text=text,buttons=[MDFlatButton(text="CLOSE", on_release = lambda *args:self.dialog.dismiss())])
            MDApp.get_running_app().dialog_text = text
            self.dialog = MDDialog(
                title=title,
                type="custom",
                content_cls = DialogContent(),
                buttons=[MDFlatButton(text="CLOSE", on_release = lambda *args:self.dialog.dismiss())]
                )
            
            #self.dialog = InfoDialog(title=title,text=text)
            self.dialog.open()

    def load_new_screen(self):
        current_screen = self.master.screen_manager.get_screen(self.master.screen_manager.current)
        current_screen.toolbar.load_new_kanji()

    # Keyboard methods

    def _keyboard_closed(self):
        #print('My keyboard have been closed!')
        #self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        #self._keyboard = None
        pass
        

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print('The key', keycode, 'have been pressed', ' - text is %r' % text, ' - modifiers are %r' % modifiers, sep="\n")
        if keycode[1] in ["left","a"]:
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
        if keycode[1] == "n": 
            self.load_new_screen()
            
    
        btn_actions = {"m":self.meanings_btn, "r":self.radicals_btn, "e":self.examples_btn}
        if keycode[1] in btn_actions:
            if isinstance(self.dialog, MDDialog): 
                self.dialog.dismiss()
            btn_actions[keycode[1]].trigger_action(0)
        # Return True to accept the key. Otherwise, it will be used by the system.
        return True
            
