from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import json

class TimerScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time_string = "0:00"
        self.time = 0
        self.running = False
        self.saved_timers = self.load_timers()

        self.add_widget(Label(text="Timer", font_size=50))

        self.timer_label = Label(text=self.time_string, font_size=50)
        self.add_widget(self.timer_label)

        self.start_stop_button = Button(text="Start", on_press=self.start_stop)
        self.add_widget(self.start_stop_button)

        self.reset_button = Button(text="Reset", on_press=self.reset)
        self.add_widget(self.reset_button)

        self.save_button = Button(text="Save", on_press=self.save)
        self.add_widget(self.save_button)

    def start_stop(self, instance):
        if not self.running:
            self.running = True
            Clock.schedule_interval(self.update_time, 1)
            instance.text = "Stop"
        else:
            self.running = False
            Clock.unschedule(self.update_time)
            instance.text = "Start"

    def update_time(self, dt):
        self.time += 1
        minutes, seconds = divmod(self.time, 60)
        self.time_string = f"{minutes}:{seconds:02d}"
        self.timer_label.text = self.time_string

    def reset(self, instance):
        if self.running:
            Clock.unschedule(self.update_time)
        self.time = 0
        self.time_string = "0:00"
        self.timer_label.text = self.time_string
        self.start_stop_button.text = "Start"
        self.running = False

    def save(self, instance):
        self.saved_timers.append(self.time_string)
        self.save_timers()

    def load_timers(self):
        try:
            with open("timers.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_timers(self):
        with open("timers.json", "w") as file:
            json.dump(self.saved_timers, file)

class TimerApp(App):
    def build(self):
        return TimerScreen()

if __name__ == "__main__":
    TimerApp().run()
