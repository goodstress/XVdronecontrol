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
        s1 = Slider(min=1400, max=2000, value=1400, orientation='vertical')
        s2 = Slider(min=1400, max=2000, value=1400, orientation='vertical')
        s3 = Slider(min=1400, max=2000, value=1400, orientation='vertical')
        s4 = Slider(min=1400, max=2000, value=1400, orientation='vertical')

        inc = NumericProperty()

        l1 = Label(text=str('idle'))
        l2 = Label(text=str('idle'))
        l3 = Label(text=str('idle'))
        l4 = Label(text=str('idle'))
        def ch_s1(instance,value):
            l1.text = str('Motor 1: %s' % (value))
        def ch_s2(instance,value):
            l2.text = str('Motor 2: %s' % (value))
        def ch_s3(instance,value):
            l3.text = str('Motor 3: %s' % (value))
        def ch_s4(instance,value):
            l4.text = str('Motor 4: %s' % (value))
        s1.bind(value=ch_s1)
        s2.bind(value=ch_s2)
        s3.bind(value=ch_s3)
        s4.bind(value=ch_s4)
        layout.add_widget(s1)
        layout.add_widget(l1)
        layout.add_widget(s2)
        layout.add_widget(l2)
        layout.add_widget(s3)
        layout.add_widget(l3)
        layout.add_widget(s4)
        layout.add_widget(l4)
        return layout

TestApp().run()
