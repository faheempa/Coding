from tkinter import *

window = Tk()
window.title("Faheem")
window.geometry("1000x500")
window.config(background="white")

menubar = Menu(window)
window.config(menu=menubar)


def open_file():
    print("Open file")


def save_file():
    print("save file")


file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(menu=file_menu, label="File")
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)


def cut_fun():
    print("Cut")


def copy_fun():
    print("Copy")


def paste_fun():
    print("Paste")


edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(menu=edit_menu, label="Edit")
edit_menu.add_command(label="Cut", command=cut_fun)
edit_menu.add_command(label="Copy", command=copy_fun)
edit_menu.add_command(label="Paste", command=paste_fun)


def print_button():
    print("clicked")


frame = Frame(window, bg="red")
frame.place(x=100, y=100)

Button(frame, text="W", command=print_button).pack(side=TOP)
Button(frame, text="A", command=print_button).pack(side=LEFT)
Button(frame, text="S", command=print_button).pack(side=LEFT)
Button(frame, text="D", command=print_button).pack(side=LEFT)


def window_fun():
    # next_window = Toplevel() # to create on top of the current window
    next_window = Tk()  # to create an independent window
    next_window.title("New window")
    next_window.geometry("800x600")
    next_window.config(background="white")
    # next_window.destroy() # to destroy window


new_window = Button(window, text="create new window", command=window_fun)
new_window.pack()

window.mainloop()
