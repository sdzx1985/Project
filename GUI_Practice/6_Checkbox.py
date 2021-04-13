from tkinter import *
import random

root = Tk()
root.title("EAT IT")
root.geometry("640x480")

chkvar = IntVar()
checkbox = Checkbutton(root, text="No more today", variable=chkvar)
# checkbox.select()
# checkbox.deselect()
checkbox.pack()

chkvar2 = IntVar()
checkbox2 = Checkbutton(root, text="No more a week", variable=chkvar2)
checkbox2.pack()

def btncmd():
    print(chkvar.get())
    print(chkvar2.get())


btn = Button(root, text="Click", command=btncmd)
btn.pack()



root.mainloop()
