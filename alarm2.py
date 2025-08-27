import unsound as us
import time
import datetime
import os
import random
import tkinter as tk

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

window = tk.Tk()
window.title("Scrappy Alarm")
window.geometry("300x300") 

# Adding input boxes
tk.Label(window, text="Hours:").pack()
hours_entry = tk.Entry(window)
hours_entry.pack()

tk.Label(window, text="Minutes:").pack()
minutes_entry = tk.Entry(window)
minutes_entry.pack()

tk.Label(window, text="Seconds:").pack()
seconds_entry = tk.Entry(window)
seconds_entry.pack()

def on_click(alarm_sound):
    print("Always ready to serve")
    alarm_sound.stop()

def start_alarm():
    hours = int(hours_entry.get())
    minutes = int(minutes_entry.get())
    seconds = int(seconds_entry.get())
    alarm(hours, minutes, seconds)

button = tk.Button(window, text="Stop", command=on_click)
button.pack(pady=10)

start_button = tk.Button(window, text="Set Alarm", command=start_alarm)
start_button.pack(pady=10)

def alarm(hours, minutes, seconds):
    now = datetime.datetime.now()
    hours = hours - now.hour
    minutes = minutes - now.minute
    seconds = seconds - now.second
    if seconds < 0:
        seconds += 60
        minutes -= 1
    if minutes < 0:
        minutes += 60
        hours -= 1
    if hours < 0:
        hours += 24
    total_seconds = hours * 3600 + minutes * 60 + seconds
    time_elapsed = random.uniform(total_seconds / 2, 3 * total_seconds / 4)
    real_time_elapsed=0

    print(CLEAR)
    while time_elapsed < total_seconds:
        time.sleep(1)
        time_elapsed += 1
        real_time_elapsed+=1

        time_left = total_seconds - time_elapsed
        hours_left = int(time_left // 3600)
        minutes_left = int((time_left % 3600) // 60)
        seconds_left = int(time_left % 60)

        print(f"{CLEAR_AND_RETURN}Alarm rings in:{hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}")

    print("Hey, just ringing here nothing to see. You can continue with whatever you were doing")
    alarm_sound = us.Sound("alarm.mp3")
    alarm_sound.play(loop=True)
    while real_time_elapsed<total_seconds:
        time.sleep(1)
        real_time_elapsed+=1
    

window.mainloop()
