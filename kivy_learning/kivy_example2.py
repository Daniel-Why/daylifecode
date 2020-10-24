from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class HomeScreen(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        # 第一行合并为一列
        layout = GridLayout(cols=1, size_hint_y=0.25)
        layout.add_widget(Label(text='My World',font_size=40))
        self.add_widget(layout)

        # 第二行 分开为 2 列
        layout_1 = GridLayout(cols=2)
        layout_1.add_widget(Button(text='Hello World 1',font_size=30))
        layout_1.add_widget(Button(text='Hello World 2',font_size=30))
        # 第三行
        layout_1.add_widget(Button(text='Hello World 4',font_size=30))
        layout_1.add_widget(Button(text='Hello World 4',font_size=30))
        self.add_widget(layout_1)

        # 第四行  分开为 3 列
        layout_2 = GridLayout(cols=3, size_hint_y=0.15)
        layout_2.add_widget(Button(text='hello',font_size=20))   # , size_hint_y=None
        layout_2.add_widget(Button(text='world',font_size=20))
        layout_2.add_widget(Button(text='hello',font_size=20))
        self.add_widget(layout_2)



class TextApp(App):
    def build(self):
        return HomeScreen()


if __name__ == '__main__':
    TextApp().run()