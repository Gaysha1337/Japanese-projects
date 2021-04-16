from logging import fatal
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput 
from kivy.clock import Clock


from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel 
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton

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

class L(MDRelativeLayout):
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        #self.adaptive_size = True

        self.textinput = HighlightText(text="愛\n14 Strokes", pos_hint={"center_x":.5, "center_y":.5})
        self.label = MDLabel(text="Sup Chad")
        self.add_widget(self.label)
        self.add_widget(self.textinput)
        self.add_widget(HighlightText(text="reeeeeeeeeeeeee", pos_hint={"center_x":.2, "center_y":.6}))

        print("lable width: ", self.label.width)

        self.focus_btn = MDFlatButton(text="Focus input", on_release = lambda *args: self.focus_input(self, self.textinput))
        self.add_widget(self.focus_btn)
    
    
    def focus_input(self, inst, input_inst):
        input_inst.focus = True if not input_inst.focus else False
        


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Pink"
        return L()

if __name__ == "__main__":
    MyApp().run()       