from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.lang import Builder


class Demo(GridLayout):
    pass


class DemoApp(App):
    def build(self):
        return Demo()


if __name__ == '__main__':
    DemoApp().run()
