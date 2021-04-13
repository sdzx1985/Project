import time
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import *
import random


root = Tk()
root.title("EAT IT")
root.geometry("640x480")


def info():
    msgbox.showinfo("Alram", "You've done your job")

def warn():
    msgbox.showwarning("WARNING", "YOU CANNOT DO THIS")

def error():
    msgbox.showerror("Error", "There are some error")

def okcancel():
    msgbox.askokcancel("OK / CANCEL", "are you sure?")

def retrycancel():
    response = msgbox.askretrycancel("RE TRY / CANCEL", "Again?")
    print("Response: ", response)
    if response == 1:
        print("ok")
    elif response == 0:
        print("no")

def yesno():
    msgbox.askyesno("YES / NO", "Again?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="Really?")
    print("Response: ", response)
    if response == 1:
        print("ok")
    elif response == 0:
        print("no")
    else:
        print("cancel")



Button(root, command=info, text="Alram").pack()
Button(root, command=warn, text="WARNING").pack()
Button(root, command=error, text="ERROR").pack()

Button(root, command=okcancel, text="confirm").pack()
Button(root, command=retrycancel, text="Re confirm").pack()
Button(root, command=yesno, text="Yes No").pack()
Button(root, command=yesnocancel, text="Yes No Cancel").pack()

root.mainloop()
