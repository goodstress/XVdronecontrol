from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import NumericProperty
class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal')
        btn1 = Button(text='arm drone')
        btn2 = Button(text='takeoff')
        btn3 = Button(text='land')
        btn4 = Button(text='disable motors')
        s = Slider(min=1400, max=2000, value=1400)
        layout.add_widget(btn1)
        layout.add_widget(btn4)
        layout.add_widget(btn3)
        layout.add_widget(btn2)
        layout.add_widget(s)
        inc = NumericProperty()
        l = Label(text=str('1400'))
        def OnSliderValueChange(instance,value):
            l.text = str(value)
        s.bind(value=OnSliderValueChange)
        layout.add_widget(l)
        return layout

TestApp().run()
