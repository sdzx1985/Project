from tkinter import *
import os

root = Tk()
root.title("No Title - Memo")
root.geometry("700x700")

filename = "myNote.txt"

# def for Menu

def fileOpen():
    if os.path.isfile(filename):
        with open(filename, "r") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())

def fileSave():
    with open(filename, "w") as file:
        file.write(txt.get("1.0", END))

# Menu 

menu = Menu(root)

menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label = "Open...", command=fileOpen)
menu_file.add_command(label = "Save", command=fileSave)
menu_file.add_separator()
menu_file.add_command(label = "Quit", command = root.quit)
menu.add_cascade(label = "File", menu = menu_file)

menu.add_cascade(label = "Edit")
menu.add_cascade(label = "Selection")
menu.add_cascade(label = "View")
menu.add_cascade(label = "Help")

# Scrollbar

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")


# Main

txt = Text(root, yscrollcommand = scrollbar.set)
txt.pack(side="left", fill="both", expand=True)
scrollbar.config(command=txt.yview)





root.config(menu=menu)
root.mainloop()


# menu_edit = Menu(menu, tearoff = 0)
# menu_selection = Menu(menu, tearoff = 0)
# menu_view = Menu(menu, tearoff = 0)
# menu_help = Menu(menu, tearoff = 0)













