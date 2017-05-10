from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn1 = Button(text='arm drone')
        btn2 = Button(text='takeoff')
        btn3 = Button(text='land')
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        return layout

TestApp().run()
