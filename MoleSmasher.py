import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import random
from functools import partial
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader

class MyButtonGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyButtonGrid, self).__init__(**kwargs)
        self.cols = 3
        self.buttons = []
        self.score = 0
        self.time= 60

        self.create_buttons()
        Clock.schedule_interval(self.create_random_button, random.uniform(1,2))  # สุ่มสร้างปุ่มทุก 1 - 2 วินาที
        Clock.schedule_interval(self.show_time,1) # จับเวลาการเล่น

        self.score_label = Label(text=f'Score: {self.score}', font_size=20)
        self.add_widget(self.score_label)  # เพิ่ม Label เข้าไปใน Grid Layout
        self.time_label = Label(text=f'Time: {self.time}', font_size=20)
        self.add_widget(self.time_label)

        # Load เสียง
        self.sound = SoundLoader.load('C:/Users/ADMIN/Desktop/nope/Metal20Pipes20Falling20Sound') 
        # Load รูปภาพ
        self.mole_image = Image(source='C:/Users/ADMIN/Desktop/nope/mole.jpg', size=(100, 100))

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
            random_button.background_normal = self.mole_image.source  # กำหนดรูปภาพเป็นพื้นหลังของปุ่ม
            Clock.schedule_once(partial(self.clear_button, random_button), 2)
    
    def clear_button(self, button, dt):
        button.text = ''
        button.background_normal = ''  # เคลียร์รูปภาพ

    def show_time(self, dt):
        self.time -= 1
        self.time_label.text = f'Time: {self.time}'
        if self.time == 0: # แสดง game over เมื่อหมดเวลา
            self.game_over()

    def game_over(self):
        self.clear_widgets()  # ลบทุก Widget ทิ้ง
        game_over_label = Label(text=f'Game Over\nScore: {self.score}', font_size=40) # แสดง game over และ คะแนนที่ได้เมื่อจบเกม
        self.add_widget(game_over_label)
    
    # ลบปุ่มที่ถูกคลิก
    def on_button_press(self, instance):

        if instance.background_normal == self.mole_image.source:
            self.score += 1
            self.score_label.text = f'Score: {self.score}'
            self.clear_button(instance, 0)

class MyApp(App):
    def build(self):
        return MyButtonGrid()

if __name__ == '__main__':
    MyApp().run()
