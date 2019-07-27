import kivy
kivy.require('1.11.1')

from kivy.app import App
#from kivy.uix.widget import Widget
#from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class MyWidget(ScreenManager):
    pass

class TestKivyApp(App):
    def build(self):
        return MyWidget()
    pass

if __name__ == "__main__":
    TestKivyApp().run()