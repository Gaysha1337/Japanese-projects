from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class MyScrollView(ScrollView):
    def on_touch_down(self, touch):
        # get touch position in coordinates of the main_box (parent of inner_scroll)
        x,y = self.ids.main_box.to_widget(*self.to_window(*touch.pos))

        # if converted position is within the inner_scroll, send touch to the inner_scroll
        if self.ids.inner_scroll.collide_point(x,y):
            touch.pos = (x,y)   # change touch position to coordinates in main_box
            return self.ids.inner_scroll.on_touch_down(touch)   # call on_touch of inner_scroll
        else:
            return super(MyScrollView, self).on_touch_down(touch)

theRoot = Builder.load_string('''
#: import Window kivy.core.window.Window
MyScrollView:
    bar_width: 5
    scroll_type:['bars', 'content']
    do_scroll: (False, True)
    size_hint_y: None
    height: Window.height
    GridLayout:
        id: main_box
        size_hint_y: None
        cols: 1
        height: self.minimum_height
        Button:
            size_hint_y: None
            height: 50
        ScrollView:
            id: inner_scroll
            bar_width: 5
            scroll_type: ['bars', 'content']
            do_scroll: (True, False)
            size_hint_y: None
            effect_cls: "ScrollEffect"
            height: Window.height/4.5
            GridLayout:
                id: horizontal_grid
                rows: 1
                padding: [10, 10]
                size: self.minimum_size
                size_hint: None, None
        Button:
            size_hint_y: None
            height: 50
''')



class ScrollTwoApp(App):
    def build(self):
        Clock.schedule_once(self.add_members)
        return theRoot

    def add_members(self, dt):
        for i in range(25):
            theRoot.ids.main_box.add_widget(Label(text='label'+str(i), size_hint=(1.0, None), height=25))
            theRoot.ids.horizontal_grid.add_widget(Label(text='Hlabel' + str(i), size_hint=(None, 1), width=75))


ScrollTwoApp().run()