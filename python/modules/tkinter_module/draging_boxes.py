from cProfile import label
from time import sleep
from tkinter import *

def bound_checking_of_a_point(x, y, px, py):
    if px>=x and px<=x+100 and py>=y and py<=y+100:
        return False
    return True

def allow_motion(bx,by,mx,my):
    if mx<bx and mx>bx+100 and my>by and my<by+100:
        return True
    return False

def new_func(newx, newy, a, b, c, d):
    if bound_checking_of_a_point(a, b, newx, newy):
        if bound_checking_of_a_point(a, b, newx+100, newy):
            if bound_checking_of_a_point(a, b, newx, newy+100):
                if bound_checking_of_a_point(a, b, newx+100, newy+100):
                    if bound_checking_of_a_point(c, d, newx, newy):
                        if bound_checking_of_a_point(c, d, newx+100, newy):
                            if bound_checking_of_a_point(c, d, newx, newy+100):
                                if bound_checking_of_a_point(c, d, newx+100, newy+100):
                                    return True

window = Tk()
window.title("Faheem")
window.geometry("1000x500")  
window.config(background="white")

def drag_start(e):
    box1.startX = e.x
    box1.startY = e.y

def motion(e):
    newx = box1.winfo_x() - box1.startX + e.x # boxinde position(relative to window) - boxil click cheyth position(relative to box) + mouse coordinates
    newy = box1.winfo_y() - box1.startY + e.y
    a = box2.winfo_x()
    b = box2.winfo_y()
    c = box3.winfo_x()
    d = box3.winfo_y()
    if new_func(newx, newy, a, b, c, d):
        box1.place(x=newx, y=newy)
    else:
        if allow_motion(a, b,newx, newy):
            if allow_motion(c,d,newx, newy):
                box1.place(x=newx, y=newy)

def drag_start2(e):
    box2.startX = e.x
    box2.startY = e.y

def motion2(e):
    newx = box2.winfo_x() - box2.startX + e.x # boxinde position(relative to window) - boxil click cheyth position(relative to box) + mouse coordinates
    newy = box2.winfo_y() - box2.startY + e.y
    a = box1.winfo_x()
    b = box1.winfo_y()
    c = box3.winfo_x()
    d = box3.winfo_y()
    if new_func(newx, newy, a, b, c, d):
        box2.place(x=newx, y=newy)
    else:
        if allow_motion(a, b,newx, newy):
            if allow_motion(c,d,newx, newy):
                box2.place(x=newx, y=newy)
            
    
box1 = Label(bg="RED", fg="black", padx=10, pady=10, width=10, height=5)
box1.place(x=0,y=0)
    
box2 = Label(bg="Blue", fg="black", padx=10, pady=10, width=10, height=5)
box2.place(x=0,y=100)


box1.bind("<Button-1>", drag_start)
box1.bind("<B1-Motion>", motion)

box2.bind("<Button-1>", drag_start2)
box2.bind("<B1-Motion>", motion2)

def drag_start(e):
    box3.startX = e.x
    box3.startY = e.y
def motion3(e):
    newx = box3.winfo_x() - box3.startX + e.x # boxinde position(relative to window) - boxil click cheyth position(relative to box) + mouse coordinates
    newy = box3.winfo_y() - box3.startY + e.y
    a = box1.winfo_x()
    b = box1.winfo_y()
    c = box2.winfo_x()
    d = box2.winfo_y()
    if new_func(newx, newy, a, b, c, d):
        box3.place(x=newx, y=newy)
    else:
        if allow_motion(a, b,newx, newy):
            if allow_motion(c,d,newx, newy):
                box3.place(x=newx, y=newy)
box3 = Label(bg="green", fg="black", padx=10, pady=10, width=10, height=5)
box3.place(x=0,y=200)

box3.bind("<Button-1>", drag_start)
box3.bind("<B1-Motion>", motion3)

window.mainloop()