from time import sleep
from tkinter import *
from PIL import Image, ImageTk

xv = 15.5
yv = 5.5
width = 1000
height = 750

window = Tk()
window.title("Animation")
window.geometry("1000x750")
window.config(background="white")

canvas = Canvas(window, width=width, height=height)
canvas.pack()

img = Image.open("/home/faheemfahi/Desktop/python/GUI/bg.png")
img = img.resize((width, height))
img_bg = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=img_bg, anchor=NW)

img = PhotoImage(file="/home/faheemfahi/Desktop/python/GUI/ufo.png")
ufo = canvas.create_image(10, 10, image=img, anchor=NW)
image_width = img.width()
image_height = img.height()


while True:
    cordinates = canvas.coords(ufo)
    if (cordinates[0] + image_width) >= width or cordinates[0] <= 0:
        xv = -xv
    if (cordinates[1] + image_height) >= height or cordinates[1] <= 0:
        yv = -yv
    canvas.move(ufo, xv, yv)
    window.update()
    sleep(0.05)

window.mainloop()