from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Faheem")
window.geometry("1000x500")
window.config(background="white")

notebook = ttk.Notebook(window)
tab_1 = Frame(notebook)
tab_2 = Frame(notebook)
notebook.add(tab_1, text="TAB 1")
notebook.add(tab_2, text="TAB 2")
notebook.pack(expand=True, fill="both")

Label(tab_1, text="hey, this tab 1", font=("Arial", 25), height=25,
      width=50).pack(side=LEFT)
Label(tab_2, text="hey, this tab 2", font=("Arial", 25), height=25,
      width=50).pack(side=LEFT)

window.mainloop()

