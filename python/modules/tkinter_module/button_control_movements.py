from tkinter import *

# on window

def move_right(e):
    label.place(x=label.winfo_x()+10)

def move_left(e):
    label.place(x=label.winfo_x()-10)

def move_up(e):
    label.place(y=label.winfo_y()-10)

def move_down(e):
    label.place(y=label.winfo_y()+10)

window = Tk()
window.title("NAME")
window.geometry("500x500")  
window.config(background="white")

img = PhotoImage(file="/home/faheemfahi/Desktop/python/GUI/car.png")
label = Label(window,image=img, border=0)
label.place(x=0,y=0)

window.bind("<Right>", move_right)
window.bind("<Left>", move_left)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)

window.mainloop()

# On canvas

def move_right(e):
    canvas.move(my_img, 10, 0)
def move_left(e):
    canvas.move(my_img, -10, 0)
def move_up(e):
    canvas.move(my_img, 0, -10)
def move_down(e):
    canvas.move(my_img, 0, 10)

window = Tk()
window.title("NAME")
window.geometry("1000x800")  
window.config(background="white")

canvas = Canvas(window,width=1000,height=800, bg="white")
canvas.pack()

img = PhotoImage(file="/home/faheemfahi/Desktop/python/GUI/car.png")
my_img = canvas.create_image(0,0,image=img, anchor=NW)

window.bind("<Right>", move_right)
window.bind("<Left>", move_left)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)

window.mainloop()


