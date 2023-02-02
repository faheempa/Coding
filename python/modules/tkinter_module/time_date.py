from time import *
from tkinter import *

def update():
    time_string = strftime("%I:%M:%S")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)
    # update the window after 1s by calling update function defined above

window = Tk()
window.title("Faheem")
window.geometry("1000x500")  
window.config(background="white")

time_label = Label(window, text="00:00:00", font=("Monospace",30), bg="black", fg="green", padx=10, pady=10)
time_label.pack()

day_label = Label(window, text="", font=("Monospace",15), bg="yellow", fg="black", padx=10, pady=10)
day_label.pack()

date_label = Label(window, text="", font=("Monospace",20), bg="black", fg="red", padx=10, pady=10)
date_label.pack()

update()

window.mainloop()

# strftime - directives
# %I - for hours
# %m - for minutes
# %S - for seconds
# %A - for name of day
# %B - name of month
# %d - date of month(1-31)
# %Y - year
