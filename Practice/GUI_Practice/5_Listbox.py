from tkinter import *
import random

root = Tk()
root.title("EAT IT")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "Apple")
listbox.insert(1, "Str")
listbox.insert(END, "Watermelon")
listbox.insert(END, "grape")
listbox.pack()

def btncmd():
    #listbox.delete()

    #print("In the list,", listbox.size())

    #print("1 ~ 3", listbox.get(0, 2))

    print("Selected", listbox.curselection())


btn = Button(root, text="Click", command=btncmd)
btn.pack()



root.mainloop()
