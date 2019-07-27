import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MyWidget(GridLayout):
    pass

class SimpleKivyApp(App):
    def build(self):
        return MyWidget()
    pass

if __name__ == "__main__":
    SimpleKivyApp().run()