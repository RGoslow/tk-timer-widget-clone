# python-tk-timer-widget
 Timer widget for tkinter.

Example usage:
 ```python
 import tkinter as tk
 import tktimerwidget

 main_window = tk.Tk()
 ##setting 'buttons' to true adds default buttons, otherwise
 ##we would have to map our own buttons.
 timer_widget = tktimerwidget.TkTimer(main_window, buttons=True)

##Class provides the following methods:
 timer_widget.start_Timer
 timer_widget.start_timer()
 timer_widget.stop_timer()
 timer_widget.reset_timer()
 ##'update_widget' updates the StringVar used by the widget, normally this
 ## gets called automatically.
 timer_widget.update_widget()
 timer_widget.add_seconds()
 timer_widget.subtract_seconds()
 timer_widget.set_elapsed()
 ```
