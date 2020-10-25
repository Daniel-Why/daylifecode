import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.widget import Widget

class OthelloGame(Widget):
    pass

class OthelloApp(App):
    def build(self):
        return OthelloGame()

if __name__ == "__main__":
    OthelloApp().run()

