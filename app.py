from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.core.text import Label as CoreLabel
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

        return layout

TestApp().run()
