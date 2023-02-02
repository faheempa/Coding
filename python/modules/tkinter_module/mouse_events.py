from tkinter import *

window = Tk()
window.title("Faheem")
window.geometry("1000x500")
window.config(background="white")

canvas = Canvas(window, height=500, width=500)
canvas.pack()
canvas.create_line(0, 0, 500, 500, fill="red", width=5)
canvas.create_line(0, 500, 250, 250, fill="blue", width=5)
canvas.create_rectangle(100, 100, 400, 400, fill="pink", width=5)
canvas.create_polygon(100,
                      400,
                      250,
                      100,
                      400,
                      400,
                      fill="black",
                      outline="white")
canvas.create_oval(200, 200, 300, 300, fill="green", width=5)
canvas.create_arc(200,
                  200,
                  300,
                  300,
                  fill="red",
                  extent=120,
                  width=5,
                  start=30)
canvas.create_arc(200,
                  200,
                  300,
                  300,
                  fill="red",
                  extent=120,
                  width=5,
                  start=210)


def mouse_click(e):
    print("mouse coordinates: " + str(e.x) + ", " + str(e.y))


window.bind("<q>", quit)
window.bind("<Button-1>", mouse_click)  # left click
window.bind("<Button-2>", mouse_click)  # scoll  click
window.bind("<Button-3>", mouse_click)  # right  click
window.bind("<ButtonRelease>", mouse_click)  # event is triggered on release of a button
window.bind("<Return>", mouse_click) # event is triggered on enter click
window.bind("<Leave>", mouse_click) # event is triggered on when the curser leaves the window
window.bind("<Motion>", mouse_click) # event is triggered on when the curser is in motion

window.mainloop()