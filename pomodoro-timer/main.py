import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

kivy.require("1.11.1")

class PomodoroTimer(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.time_minutes = 25
        self.time_seconds = 00
        self.time = 60 * self.time_minutes + self.time_seconds
        self.working = True
        self.label = Label(text="25:00", font_size=30)
        self.add_widget(self.label)
        self.button = Button(text="Start", font_size=30)
        self.button.bind(on_press=self.start)
        self.add_widget(self.button)


    def update_time(self, dt):
        self.time_minutes = int((self.time - self.time % 60) / 60)
        self.time_seconds = self.time % 60
        if self.time == 0:
            self.working = not self.working
            if self.working:
                self.time_minutes = 25
                self.time_seconds = 0
                self.label.text = "25:00"
            else:
                self.time_minutes = 5
                self.time_seconds = 0
                self.label.text = "05:00"
        else:
            self.time -= 1
            if self.time_minutes < 10:
                self.time_label_minutes = "0" + str(self.time_minutes)
            else:
                self.time_label_minutes = str(self.time_minutes)
            if self.time_seconds < 10:
                self.time_label_seconds = "0" + str(self.time_seconds)
            else:
                self.time_label_seconds = str(self.time_seconds)
            self.label.text = self.time_label_minutes + ":" + self.time_label_seconds

# 開発中

    def start(self, instance):
        Clock.schedule_interval(self.update_time, 1)
        self.button.text = "Running"
        self.button.unbind(on_press=self.start)

class PomodoroTimerApp(App):
    def build(self):
        return PomodoroTimer()

if __name__ == "__main__":
    PomodoroTimerApp().run()
