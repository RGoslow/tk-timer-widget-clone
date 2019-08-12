import tkinter as tk
from time import time, sleep
from datetime import timedelta
import threading

class Timer():
    def __init__(self):
        ##Set up instance variables
        self._timer_epoch = 0
        self._time_paused = 0
        self._time_added = 0
        self._time_elapsed = 0
        self._running = False


    def start_timer(self):
        ##Don't start a new thread if we're already running.
        if not self.is_running():
            self._running = True
            self._timer_epoch = time()
            thread = threading.Thread(target=self.run)
            thread.start()

    def update_timer(self):
        self._time_elapsed = time() - self._timer_epoch + self._time_paused + self._time_added

    def stop_timer(self):
        self._time_paused = self._time_elapsed
        self._running = False

    def reset_timer(self):
        self._time_elapsed = 0
        self._time_paused = 0
        self._time_added = 0

    def add_seconds(self, seconds_to_add):
        self._time_added += seconds_to_add

    def subtract_seconds(self, seconds_to_subtract):
        self._timer_added -= seconds_to_subtract

    def set_elapsed(self, time_in_seconds ):
        self.reset_timer()
        self._timer_epoch = time() - time_in_seconds
        self.update_timer()

    def is_running(self):
        return self._running

    def get_elapsed(self):
        date_time_str = str(timedelta(seconds=self._time_elapsed))
        return (self._time_elapsed, date_time_str)

    def run(self, external_time_in_seconds = None, update_rate = 0.009):
        self._timer_epoch = time()
        while self.is_running():
            if external_time_in_seconds is None:
                self.update_timer()
            else:
                self.set_elapsed(external_time_in_seconds)
            sleep(update_rate)
