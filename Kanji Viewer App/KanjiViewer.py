from kivymd.app import MDApp
from kivymd.toast.kivytoast.kivytoast import toast

# Layouts
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.gridlayout import MDGridLayout

# Widgets
from kivymd.uix.button import MDIconButton, MDRectangleFlatIconButton, MDRectangleFlatButton
from kivymd.uix.label import MDLabel, Label
from kivy.uix.image import AsyncImage
from kivy.uix.carousel import Carousel
from kivy.uix.scrollview import ScrollView

# Utils
from utils import get_kanji_data, get_kanji_from_level
from kivy.clock import Clock


class StrokeImage(AsyncImage):
    def __init__(self, source,width=200, height=200, **kwargs):
        super().__init__(**kwargs)
        self.source = source
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
        self.master = master
        self.level = level

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
            
            self.kanji_layout.add_widget(Label(text=str(self.kanji), font_size=75,halign="center", pos_hint={"center_y":.8}))
            self.kanji_layout.add_widget(Label(text=str(self.stroke_count), font_size=20,halign="center", pos_hint={"center_y":.7}))
            
            self.carousel = KanjiStrokeImageCarousel(self.stroke_order_images)
            self.kanji_layout.add_widget(self.carousel)
            self.prev_btn = MDIconButton(icon="menu-left", user_font_size ="200sp", on_release = lambda x:self.carousel.load_previous(), pos_hint={"center_x":.1, "center_y":.5}) # pos_hint={"left":.2, "y":.5},
            self.next_btn = MDIconButton(icon="menu-right", user_font_size ="200sp", on_release = lambda x:self.carousel.load_next(), pos_hint={"center_x":.9, "center_y":.5}) # pos_hint={"right":.8, "y":.5}
            self.kanji_layout.add_widget(self.prev_btn)
            self.kanji_layout.add_widget(self.next_btn)
            print(self.kanji)

            for i, reading in enumerate(self.readings):
                self.kanji_layout.add_widget(Label(text=reading,font_size=20, pos_hint={"center_x":.5,"center_y":.3-(i/20)}))
            
            self.kanji_layout.add_widget(Label(text="Radical Info",font_size=20 ,pos_hint={"center_x":.5,"center_y":.2}))
            for i, rad in enumerate(self.radicals_data):
                #self.kanji_layout.add_widget(MDLabel(text=str(rad), font_size=12 ,pos_hint={"center_x":.5,"center_y":.2-(i/20)}))
                pass
            #print(self.radicals_data, "\n")
            #print(" ".join([j for j in [" ".join(i) for i in self.radicals_data]]))
            formated_radicals = " \n".join([rad for rad in [":".join(tup) for tup in self.radicals_data]])
            self.kanji_layout.add_widget(Label(text=formated_radicals,halign="center", font_size=15, pos_hint={"center_x":.5,"center_y":.1}))
            
            self.add_widget(self.kanji_layout)

            