from tkinter import *
from pynput.keyboard import Key, Controller
import time
import pyautogui
import numpy as np

root = Tk()

bool_grid = np.ndarray((8, 8), dtype = bool)

root.title("Music Machine")
root.geometry("780x860+500+40")

label_interval = Label(root, text = "Enter time interval: ", font = ("arial", 20, "bold"), fg = "black").place(x = 10, y = 10)
label_suggested = Label(root, text = "(suggested: )", font = ("arial", 15), fg = "grey").place(x = 320, y = 10)

time_interval = DoubleVar()

interval_box = Entry(root, textvariable = time_interval, width = 5).place(x = 250, y = 10)

def start_music():
    print('music started')

def create_buttons():
    print('buttons created')
    for j in range(8):
        for i in range(8):
            self.btn[j][i] = Button (root, bg = 'black', width = 6, height = 3, command = lambda x=j, y=i: self.but_pressed(x, y)).place(x = 10 + i*100 , y = 100 + j*100)
            bool_grid[i][j] = False

def but_pressed(self, x, y):
    print('button pressed: ' + str(x) + ', ' + str(y))
    bool_grid[x][y] = not bool_grid[x][y]
    print(bool_grid)
    self.button.configure(bg = "red")

generateMusic = Button(root, text = "Begin", width = 30, height = 2, bg = 'lightblue', command = start_music).place(x = 470, y = 10)

create_buttons()

root.mainloop()