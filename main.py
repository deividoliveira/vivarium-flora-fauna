from kivy.app import App
from kivy.uix.label import Label


class VivariumApp(App):

  def build(self):
    return Label(
        text='Vivarium Flora e Fauna\nBem-vindo ao seu app!',
        font_size='24sp',
        halign='center',
    )


if __name__ == '__main__':
  VivariumApp().run()
