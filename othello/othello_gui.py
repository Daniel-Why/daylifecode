from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button

label_game_name='[font=Lobster-Regular][i]Dinasour[/i][/font] [size=30sp][color=#a7324a][b]Egg[/b][/color][/size]'
label_creator='[font=OCRAEXT]Fatzero[/font]'

class FirstScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title='Othello'
        self.cols = 1
        # layout = GridLayout(cols=1)
        lab_game_name = Label(text=label_game_name,markup=True,font_size='25sp',size_hint_y=None,height=100)
        lab_creator = Label(text=label_creator,markup=True,font_size='20sp',size_hint_y=None,height=100)
        img_logo = Image(source='.\\othello\\static\\othello.png',size_hint_y=None,height=350)
        lab_start_button=Button(text='START',size_hint_y=None,height=10)

        self.add_widget(lab_game_name)
        self.add_widget(img_logo)
        self.add_widget(lab_start_button)
        self.add_widget(lab_creator)

class OthelloApp(App):
    def build(self):
        return FirstScreen()
if __name__ == "__main__":
    OthelloApp().run()

