from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder


class CustomScreen(Screen):
    hue = NumericProperty(0)


class ScreenKivyApp(App):

    def build(self):
        MyScrMgr = ScreenManager()
        MyScrMgr.add_widget(CustomScreen(name='Home'))
        MyScrMgr.add_widget(CustomScreen(name='Screen1'))
        return MyScrMgr


if __name__ == '__main__':
    ScreenKivy
    App().run()
