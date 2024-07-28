from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


class Application(App):


    def build(self):

        but_together = BoxLayout()
        grid = GridLayout(cols=1)

        my_but = Button(text="Нажми меня срочно!", font_size=30, background_color="cyan")
        think_of_name = Button(text="Не нажимай меня!", font_size=30, background_color="cyan")
        label = Label(text="Текст", font_size=30)

        but_together.add_widget(my_but)
        but_together.add_widget(think_of_name)
        #but_together.add_widget(label)

        grid.add_widget(but_together)
        grid.add_widget(label)

        return grid


if __name__ == "__main__":
    Application().run()