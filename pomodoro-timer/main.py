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
        self.time = 25
        self.working = True
        self.label = Label(text="25:00", font_size=30)
        self.add_widget(self.label)
        self.button = Button(text="Start", font_size=30)
        self.button.bind(on_press=self.start)
        self.add_widget(self.button)

    def update_time(self, dt):
        if self.time == 0:
            self.working = not self.working
            if self.working:
                self.time = 25
                self.label.text = "25:00"
            else:
                self.time = 5
                self.label.text = "05:00"
        else:
            self.time -= 1
            if self.time < 10:
                self.label.text = "0" + str(self.time) + ":00"
            else:
                self.label.text = str(self.time) + ":00"

    def start(self, instance):
        Clock.schedule_interval(self.update_time, 1)
        self.button.text = "Running"
        self.button.unbind(on_press=self.start)

class PomodoroTimerApp(App):
    def build(self):
        return PomodoroTimer()

if __name__ == "__main__":
    PomodoroTimerApp().run()
