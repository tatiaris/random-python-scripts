from tkinter import *
from pynput.keyboard import Key, Controller
import time
import pyautogui

keyboard = Controller()
root = Tk()

root.title("Type Machine")
root.geometry("800x180+500+900")

label_text = Label(root, text = "Enter text to be typed: ", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 10)
label_interval = Label(root, text = "Enter time interval: ", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 40)
label_suggested = Label(root, text = "(suggested: 0.088)", font = ("arial", 15), fg = "grey").place(x = 320, y = 40)

user_input = StringVar()
time_interval = DoubleVar()

entry_box = Entry(root, textvariable = user_input, width = 50).place(x = 250, y = 10)
interval_box = Entry(root, textvariable = time_interval, width = 5).place(x = 250, y = 40)

def start_typing():
    time.sleep(2)
    passage = str(user_input.get())
    tInterval = float(time_interval.get())
    while len(passage) > 0:
        front = passage[0]
        if front.islower():
            keyboard.press(front)
        elif front.isupper():
            keyboard.press(Key.shift)
            keyboard.press(front.lower())
            keyboard.release(Key.shift)
        else:
            pyautogui.press(front)
        time.sleep(tInterval)
        passage = passage[1:]

type = Button(root, text = "Begin", width = 30, height = 5, bg = 'lightblue', command = start_typing).place(x = 250, y = 70)

root.mainloop()