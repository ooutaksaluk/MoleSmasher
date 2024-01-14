import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import random
from functools import partial

class MyButtonGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyButtonGrid, self).__init__(**kwargs)
        self.cols = 3
        self.buttons = []
        self.score = 0
        self.time=60

        self.create_buttons()
        Clock.schedule_interval(self.create_random_button, random.uniform(1,2))  # สุ่มสร้างปุ่มทุก 1 - 2 วินาที

        self.score_label = Label(text=f'Score: {self.score}', font_size=20)
        self.add_widget(self.score_label)  # เพิ่ม Label เข้าไปใน Grid Layout
        self.time_label = Label(text=f'Time: {self.time}', font_size=20)
        self.add_widget(self.time_label)

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
            Clock.schedule_once(partial(self.clear_button, random_button), 2)
    
    def clear_button(self, button, dt):
        if button.text == 'Mole':
            button.text = ''
    

    # ลบปุ่มที่ถูกคลิก
    def on_button_press(self, instance):
        if instance.text == 'Mole':
            self.score += 1
            self.remove_widget(self.score_label)  # ลบ Label ทิ้ง
            self.score_label = Label(text=f'Score: {self.score}', font_size=20)  # สร้าง Label ใหม่
            self.add_widget(self.score_label)  # เพิ่ม Label เข้าไปใน Grid Layout
        instance.text = ''

class MyApp(App):
    def build(self):
        return MyButtonGrid()

if __name__ == '__main__':
    MyApp().run()
