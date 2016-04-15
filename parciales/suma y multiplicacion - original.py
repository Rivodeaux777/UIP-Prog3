from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

x = Builder.load_file("calc.kv")

class Calc(FloatLayout):
    def product(self, instance,):

        self.result.text = str(int(self.a.text) * int(self.b.text))

class TestApp(App):
    def build(self):
        return Calc()

if __name__ == '__main__':
    TestApp().run()
