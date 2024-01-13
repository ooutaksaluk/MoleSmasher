import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.clock import Clock
import random

class MyButtonGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyButtonGrid, self).__init__(**kwargs)
        self.cols = 3
        self.buttons = []
        self.create_buttons()
        Clock.schedule_interval(self.create_random_button, 1.5)  #สร้างปุ่มทุก 1.5 วินาที

    def create_buttons(self):
        for i in range(9):
            button = Button(text='', on_press=self.on_button_press)
            self.buttons.append(button)
            self.add_widget(button)
# สุ่มตำแหน่งของปุ่ม
    def create_random_button(self, dt):
        available_buttons = [b for b in self.buttons if b.text == '']
        if available_buttons:
            random_button = random.choice(available_buttons)
            random_button.text = 'Mole'
#ลบปุ่มที่ถูกคลิก
    def on_button_press(self, instance):
        instance.text = ''


class MyApp(App):
    def build(self):
        return MyButtonGrid()


if __name__ == '__main__':
    MyApp().run()