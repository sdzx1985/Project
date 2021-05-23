import time
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import *
import random


root = Tk()
root.title("EAT IT")
root.geometry("640x480")

Label(root, text="Select the menu").pack(side="top")

Button(root, text="Order").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="Hamburger").pack()
Button(frame_burger, text="Cheese burger").pack()
Button(frame_burger, text="Chicken burger").pack()

frame_drink = LabelFrame(root, text="Drink")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="Coke").pack()
Button(frame_drink, text="Sprite").pack()




root.mainloop()
