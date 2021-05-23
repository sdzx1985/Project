from tkinter import *

root = Tk()
root.title("EAT IT")
root.geometry("640x480")

label1 = Label(root, text="Hi")
label1.pack()

photo = PhotoImage(file="/Users/aidenoh/Documents/GitHub/GUI_Basic/CheckImage.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="See you again")

    global photo2
    photo2 = PhotoImage(file="/Users/aidenoh/Documents/GitHub/GUI_Basic/CancleImage.png")
    label2.config(image=photo2)

btn = Button(root, text="Click", command=change)
btn.pack()

root.mainloop()
