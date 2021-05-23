import time
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import *
import random


root = Tk()
root.title("EAT IT")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range (1, 32):
    listbox.insert(END, str(i) + "th")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

root.mainloop()
