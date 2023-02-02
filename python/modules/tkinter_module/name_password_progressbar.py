import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar

window = Tk()
window.title("Faheem")
window.geometry("1000x500")
window.config(background="white")
fname_label = Label(text=" First Name  : ",
                    font=("Monospace", 15),
                    bg="Black",
                    fg="White",
                    padx=10,
                    pady=10)
fname_label.grid(row=0, column=0)
fname = Entry(window,
              font=("Arial", 20),
              fg="red",
              bg="black",
              width=20,
              borderwidth=8)
fname.grid(row=0, column=1)
lname_label = Label(text=" Last Name   : ",
                    font=("Monospace", 15),
                    bg="Black",
                    fg="White",
                    padx=10,
                    pady=10)
lname_label.grid(row=1, column=0)
lname = Entry(window,
              font=("Arial", 20),
              fg="red",
              bg="black",
              width=20,
              borderwidth=8)
lname.grid(row=1, column=1)
email_label = Label(text=" Email       : ",
                    font=("Monospace", 15),
                    bg="Black",
                    fg="White",
                    padx=10,
                    pady=10)
email_label.grid(row=2, column=0)
email = Entry(window,
              font=("Arial", 20),
              fg="red",
              bg="black",
              width=20,
              borderwidth=8)
email.grid(row=2, column=1)
password_label = Label(text=" Password    : ",
                       font=("Monospace", 15),
                       bg="Black",
                       fg="White",
                       padx=10,
                       pady=10)
password_label.grid(row=3, column=0)
password = Entry(window,
                 font=("Arial", 20),
                 fg="red",
                 bg="black",
                 width=20,
                 show="#",
                 borderwidth=8)
password.grid(row=3, column=1)


def submit_fun():
    bar.config(value=0)
    percentage_value = 0
    for i in range(10):
        bar["value"] += 10  # add by 10%
        percentage_value += 10
        percentage.config(text=str(percentage_value) + "%")
        window.update_idletasks()
        time.sleep(0.2)
    if fname.get()=="" or lname.get()=="" or email.get()=="" or password.get()=="":
        message = messagebox.showinfo(title="incomplete !!", message="Enter complete details")
        return
    print("-"*50)
    print(fname.get())
    print(lname.get())
    print(email.get())
    print(password.get())
    fname.delete(0, END)
    lname.delete(0, END)
    email.delete(0, END)
    password.delete(0, END)
    fname.focus_set()



submit = Button(window,
                text="Submit",
                command=submit_fun,
                font=("comic sans", 15),
                fg="#0c0091",
                bg="#36ffe1",
                activeforeground="#73fff6",
                activebackground="#3f2eff")
submit.grid(row=4, column=0, columnspan=2)

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.grid(row=5, column=0, columnspan=2)

percentage = Label(text="0%",
                   font=("Monospace", 15),
                   bg="white",
                   fg="black",
                   padx=10,
                   pady=10)
percentage.grid(row=6, column=0, columnspan=2)

fname.focus_set()


def focus(e):
    if window.focus_get() == fname:
        lname.focus_set()
        return
    if window.focus_get() == lname:
        email.focus_set()
        return
    if window.focus_get() == email:
        password.focus_set()
        return
    if window.focus_get() == password:
        submit_fun()
        return



window.bind("<Return>", focus)

window.mainloop()
