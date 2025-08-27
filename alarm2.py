import winsound
import time
import datetime
import os
import random
import tkinter as tk


window = tk.Tk()
window.title("Scrappy Alarm")
window.geometry("300x300")

tk.Label(window, text="Hours:").pack()
hours_entry = tk.Entry(window)
hours_entry.pack()

tk.Label(window, text="Minutes:").pack()
minutes_entry = tk.Entry(window)
minutes_entry.pack()

tk.Label(window, text="Seconds:").pack()
seconds_entry = tk.Entry(window)
seconds_entry.pack()

def start_alarm():
        global hours,minutes,seconds
        hours = int(hours_entry.get())
        minutes = int(minutes_entry.get())
        seconds = int(seconds_entry.get())
        import threading
        threading.Thread(target=alarm, args=(hours, minutes, seconds), daemon=True).start()

def play_sound():
    winsound.PlaySound("alarm.wav",winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)

def stop_sound():
    winsound.PlaySound(None,winsound.SND_PURGE)


start_button = tk.Button(window, text="Set Alarm", command=start_alarm) 
start_button.pack(pady=10)
button = tk.Button(window, text="Stop", command=stop_sound) 
button.pack(pady=10)


message_label = tk.Label(window, text="", font=("Arial", 12))
message_label.pack(pady=10)

alarm_sound = None
orange_button = None
alarm_looping = False


def on_orange_click():
    global alarm_sound
    now = datetime.datetime.now().strftime("%H:%M:%S")
    message_label.config(text=f"It's already {now}!")
    play_sound



button = tk.Button(window, text="Stop", command=stop_sound)
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
    hours=hours-6
    minutes=minutes-40
    seconds=seconds-30
    total_seconds = hours * 3600 + minutes * 60 + seconds
    time_elapsed = random.uniform(total_seconds // 4, total_seconds // 2)
    real_time_elapsed = 0

    while time_elapsed < total_seconds:
        time.sleep(1)
        time_elapsed += 1
        real_time_elapsed += 1

        time_left = total_seconds - real_time_elapsed
        hours_left = int(time_left // 3600)
        minutes_left = int((time_left % 3600) // 60)
        seconds_left = int(time_left % 60)

        message_label.config(text=f"Alarm rings in: {hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}")
    
    message_label.config(text=f"Hey, just ringing here nothing to see. You can continue with whatever you were doing")
    alarm_looping = True
    play_sound()
    global orange_button, alarm_sound

    def show_orange_button():
        window.configure(bg="orange")
        if orange_button is None:
            orange_button = tk.Button(window, bg="orange", activebackground="orange", borderwidth=0,
                                     command=on_orange_click)
            orange_button.place(relx=0, rely=0, relwidth=1, relheight=1)
        else:
            orange_button.lift()
        message_label.config(text="")
    while real_time_elapsed<total_seconds:
        real_time_elapsed+=1
    window.after(0, show_orange_button)

window.mainloop()
