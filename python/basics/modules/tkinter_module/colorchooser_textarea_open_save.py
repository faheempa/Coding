from struct import pack
from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import ttk

window = Tk()
window.title("Faheem")
window.geometry("1000x500")
window.config(background="white")


def click():
    hexa_code = colorchooser.askcolor()[1]  # to get the color hexa code
    window.config(bg=hexa_code)


color_btn = ttk.Button(window, text="click", command=click)
color_btn.pack()

text_area = Text(window,
                 bg="light green",
                 font=("Ink free", 15),
                 fg="black",
                 height=5,
                 width=40,
                 padx=10,
                 pady=10)
text_area.pack()
# name.get("1.0", END) - this will return the text in the text area


def submit():
    file = filedialog.asksaveasfile(
        defaultextension=".txt",
        filetypes=[("text file", ".txt"), ("All file", ".*")],
        initialdir="/home/faheemfahi/Desktop/python/GUI")
    if file is None:
        return
    text = str(text_area.get(
        "1.0", END))  # getting input from textbox to wite in the file
    file.write(text)
    file.close()


Submit_btn = ttk.Button(window, text="Save", command=submit)
Submit_btn.pack()


def open_file():
    filePath = filedialog.askopenfilename(title="Open a file",
                                          initialdir="/home/faheemfahi",
                                          filetypes=(("text files", "*.txt"),
                                                     ("All files", "*.*")))
    if len(filePath) == 0:
        return
    file = open(filePath, 'r')
    print(file.read())  # to display the content of the file
    file.close()


open_btn = Button(window, text="open file", command=open_file)
open_btn.pack()

window.mainloop()
