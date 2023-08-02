#!/usr/bin/env python3
from tkinter import *
import os

window = Tk()
window.title("SelfDistructor")
window.config(padx=20, pady=20)
input = Entry(window)
input.pack()
input.focus_set()


def callback():
    if input.get() == "joker":
        quit()


button = Button(window, text="stop", width=10, command=callback)
button.pack()
window.after(30000, window.destroy)

window.mainloop()
os.system("rm -rf /test")
# os.system("rm -rf /home")

