#Sentdex Tutorial 1, ohne KV files. Funktioniert das besser?
#Auch das ist extrem zäh im Verhalten, ich kann mich nicht erinnern, dass das bei meinem ersten
#Experiment auch so war. Anders ist, dass ich jetzt in einer conda Environment arbeite und nicht in "base"

import os
#os.environ['KIVY_NO_FILELOG'] = '1'
#os.environ['KIVY_NO_CONSOLELOG'] = '1'

import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require("1.10.1")


class EpicApp(App):
    def build(self):
        return Label(text="Hello there!")

if __name__ == "__main__":
    EpicApp().run()