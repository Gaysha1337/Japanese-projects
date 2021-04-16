from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout

from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton

#import MDBoxLayout kivymd.uix.boxlayout.MDBoxLayout
KV = '''

<Content>
    orientation: "vertical"
    height: "120dp"
    spacing: "12dp"
    size_hint_y: None
    
    HighlightText:
        text: "City"

    HighlightText:
        text: "Street"

MDFloatLayout:

    MDFlatButton:
        text: "ALERT DIALOG"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_confirmation_dialog()
'''
class HighlightText(MDTextField):
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)

        self.readonly = True
        self.cursor_blink = False
        self.cursor_color = (0,0,0,0)
        self.active_line = False
        self.line_color_normal = (0,0,0,0)
        self.halign = "center"
        #self.mode = "rectangle"
        #self.pos_hint = {"center_x":.5, "center_y":.5}
        self.size_hint_x = 0.11 * len(self._lines)
        
        self.allow_copy = True
        #self.disabled = True

    def on_selection_text(self, instance, value):
        super().on_selection_text(instance, value)
        if self._selection_finished:
            print("selection finished")
            #self.focus = False

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and (not touch.is_double_tap or not touch.is_triple_tap):
            self.focus = False 

        if touch.is_double_tap and self.collide_point(*touch.pos):
            self.select_all()
        return super().on_touch_down(touch)
    
    def on_touch_move(self, touch):
        if touch.is_double_tap or self.collide_point(*touch.pos):
            pass
            #self.select_all()      
            #self.select_text(self.cursor_offset(), self.cursor_index())
            #print(self.cursor_offset())
            
        return super().on_touch_move(touch)


class Item(OneLineAvatarListItem):
    divider = None
    #source = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(HighlightText())


class Content(MDBoxLayout):
    #pass
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.adaptive_height = True
        #self.add_widget(HighlightText(text="whfkuwh"))


class Example(MDApp):
    dialog = None

    def build(self):
        return Builder.load_string(KV)

    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Address:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color
                    ),
                ],
            )
        self.dialog.open()


Example().run()