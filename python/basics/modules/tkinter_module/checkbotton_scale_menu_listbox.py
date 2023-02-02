from tabnanny import check
from tkinter import *

window = Tk()
window.title("FAHEEM")
window.geometry("1000x500")
window.config(background="white")

x = BooleanVar()


def status():
    print(x.get())


box = Checkbutton(window,
                  text="Check this",
                  variable=x,
                  onvalue="True",
                  offvalue="False",
                  command=status,
                  font=("monospace", 15),
                  fg="red",
                  bg="blue",
                  activeforeground="red",
                  activebackground="blue",
                  padx=10,
                  pady=10)
box.pack()

scale = Scale(window,
              from_=0,
              to=100,
              orient=HORIZONTAL,
              font=("monospace", 15),
              length=500)
scale.pack()


def submit():
    print(scale.get())


submit = Button(window, text="submit", command=submit)
submit.pack()

xy = IntVar()
menu = ["A", "B", "C", "D"]
for i in range(len(menu)):
    radio = Radiobutton(
        window,
        text=menu[i],
        variable=xy,
        value=i,
        font=("arial", 15),
        fg="red",
        bg="black",
        padx=10,
        pady=10,
        # use command= to assign some function for each click
    )
    radio.pack(anchor=W)  # W for west

listbox = Listbox(window,
                  bg="#6beefa",
                  font=("arial", 15),
                  width=15,
                  selectmode=SINGLE)
listbox = Listbox(window, bg="#6beefa", font=("arial",15), width=15, selectmode=SINGLE)
listbox.pack()
listbox.insert(1,"A")
listbox.insert(2,"B")
listbox.insert(3,"C")
listbox.config(height=listbox.size())
# to access selected index - name.curselection()
# to access the selected element - name.get(name.surselection())
# to delete the selected element - name.delete(name.curselection)
# during multiple selection use loop through each of the elements - for index in name.curselection():
# and each element can be accessed inside the loop using - name.get(index)


def list_submit():
    print(listbox.get(listbox.curselection()))


list_submit = Button(window, text="Submit", command=list_submit)
list_submit.pack()


def list_delete():
    if listbox.size() != 0 and listbox.curselection():
        listbox.delete(listbox.curselection())
        listbox.config(height=listbox.size())
    else:
        print("Nothing to delete")


del_btn = Button(window, text="Delete", command=list_delete)
del_btn.pack()

list_entry = Entry(window, font=(" arial", 20), fg="red", bg="black")
list_entry.pack()


def list_insert():
    listbox.insert(listbox.size(), list_entry.get())
    listbox.config(height=listbox.size())


list_add = Button(window, text="Add", command=list_insert)
list_add.pack()

window.mainloop()
