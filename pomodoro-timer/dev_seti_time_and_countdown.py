from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.textinput import TextInput

class TimerScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time_string = "0:00"
        self.time = 0
        self.running = False

        self.add_widget(Label(text="Enter time (mm:ss):"))

        self.time_input = TextInput(text="0:00")
        self.add_widget(self.time_input)

        self.start_button = Button(text="Start", on_press=self.start)
        self.add_widget(self.start_button)

        self.timer_label = Label(text=self.time_string, font_size=50)
        self.add_widget(self.timer_label)

    def start(self, instance):
        if not self.running:
            self.running = True
            self.time = int(self.time_input.text.split(":")[0]) * 60 + int(self.time_input.text.split(":")[1])
            Clock.schedule_interval(self.update_time, 1)

    def update_time(self, dt):
        self.time -= 1
        if self.time < 0:
            Clock.unschedule(self.update_time)
            self.running = False
        minutes, seconds = divmod(self.time, 60)
        self.time_string = f"{minutes}:{seconds:02d}"
        self.timer_label.text = self.time_string

class TimerApp(App):
    def build(self):
        return TimerScreen()

if __name__ == "__main__":
    TimerApp().run()
