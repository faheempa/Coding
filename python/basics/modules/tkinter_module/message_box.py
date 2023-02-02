from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Faheem")
window.geometry("1000x500")
window.config(background="white")


def click():
    messagebox.showerror(title="error", message="this is an error")

    messagebox.showinfo(title="info", message="this is an info")

    messagebox.showinfo(title="warning", message="this is a warning")

    if messagebox.askokcancel(title="title", message="message"):
        print("ok")
    else:
        print("cancel")

    ans = messagebox.askquestion(title="title", message="message")
    if ans =="yes":
        print("yes")
    else:
        print("no")

    if messagebox.askretrycancel(title="title", message="message"):
        print("retry")
    else:
        print("Cancel")

    if messagebox.askyesno(title="title", message="message"):
        print("Yes")
    else:
        print("No")

    reply = messagebox.askyesnocancel(title="title", message="message", icon="warning")
    if reply==True:
        print("yes")
    elif reply==False:
        print("No")
    else:
        print("cancel")


clickbutton = Button(window, text="click here", command=click)
clickbutton.pack()

window.mainloop()