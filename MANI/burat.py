from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class TarubLayout(BoxLayout):
    count = 0

    def increase(self):
        self.count += 1
        self.ids.output.text = f"Count: {self.count}"

class BuratApp(App):
    def build(self):
        return Builder.load_file("tarub.kv")

if __name__ == "__main__":
    BuratApp().run()
