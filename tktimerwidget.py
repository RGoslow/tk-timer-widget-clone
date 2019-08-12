import tkinter as tk
from timer import Timer

class TkTimer(object):
    """docstring for TkTimer."""

    def __init__(self, root=None, buttons=False):
        if root is None:
            self.root = tk.Tk()
        else:
            self.root = root
        ##Set up instance variables
        self.timer = Timer()

        ##Set up tkinter widgets:
        self.widget = tk.Frame(self.root)
        self._timer_stringvar = tk.StringVar()
        self._timer_stringvar.set("00:00:00.00")
        self._timer_label = tk.Label(self.widget, textvariable=self._timer_stringvar)
        self._timer_label.pack()

        if buttons:
            play_btn = tk.Button(self.widget, text="Start", command=self.start_timer)
            play_btn.pack()
            stop_btn = tk.Button(self.widget, text="Stop", command=self.stop_timer)
            stop_btn.pack()
            reset_btn = tk.Button(self.widget, text="Reset", command=self.reset_timer)
            reset_btn.pack()

        self.widget.pack()

    def start_timer(self):
        if not self.timer.is_running():
            self.timer.start_timer()
            self.run_loop()

    def stop_timer(self):
        self.timer.stop_timer()

    def reset_timer(self):
        self.timer.reset_timer()
        self.update_widget(True)

    def update_widget(self, force_update = False):
        if self.timer.is_running() or force_update:
            __, elapsed_str = self.timer.get_elapsed()
            self._timer_stringvar.set(elapsed_str)
    def set_elapsed(self, time_in_seconds):
        self.timer.set_elapsed(time_in_seconds)
        self.update_widget(True)

    def add_seconds(self, seconds_to_add):
        self.timer.add_seconds(seconds_to_add)
        self.update_widget(True)

    def subtract_seconds(self, seconds_to_subtract):
        self.timer.subtract_seconds(seconds_to_subtract)
        self.update_widget(True)

    def run_loop(self):
        if self.timer.is_running():
            self.update_widget()
            self.root.after(1, self.run_loop)
