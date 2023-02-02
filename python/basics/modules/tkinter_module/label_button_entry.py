from tkinter import *

window = Tk()
# instantiate an instance of window

window.geometry("800x800")  #setting size
window.title("FAHEEM")

icon = PhotoImage(
    file="/home/faheemfahi/Desktop/python/GUI/logo.png")  #setting window icon
window.iconphoto(True, icon)

window.config(background="#5962ff")

label = Label(window, text="HELLO WORLD", font=("monospace", 25))
# label.pack() // to place the label in the middle of the window
label.place(x=300, y=200)  #to place at a location

count = 0


def click():  #define click action for button
    global count
    count += 1
    print(count)


# img = PhotoImage(file='/home/faheemfahi/Desktop/python/GUI/logo.png')

# making a button
btn = Button(
    window,
    text="click here",
    command=click,
    font=("comic sans", 20),
    fg="green",
    bg="black",
    activeforeground="black",
    activebackground="green",
    state=ACTIVE
    #  image=img
)
btn.pack()

# entry box
entry = Entry(window, font=("arial", 30), fg="red", bg="black")
entry.pack(side=LEFT)


#delete button
def delete():
    entry.delete(0, END)


delete_btn = Button(window, text="Delete", command=delete)
delete_btn.pack(side=RIGHT)


def backspace():
    entry.delete(len(entry.get()) - 1, END)


backspace = Button(window, text="backspace", command=backspace)
backspace.pack(side=RIGHT)

password = Entry(window, font=("arial", 30), fg="red", bg="black", show="*")
password.place(x=0, y=450)


# submit button
def submit():
    username = entry.get()
    passwd = password.get()
    print("Username: " + username)
    print("Password: " + passwd)
    entry.config(state=DISABLED)


submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

window.mainloop()  #to run windowlen
