from tkinter import *
from ball import *
import time

def collision_testing(a, b):
    c1 = a.center()
    c2 = b.center()
    distance = (((c1[0]-c2[0])**2)+((c1[1]-c2[1])**2))**0.5
    if distance <= a.radius() + b.radius():
        a.change()
        b.change()
        
window = Tk()
window.title("Faheem")
window.geometry("500x500")
window.config(background="white")

canvas = Canvas(window, height=500, width=500)
canvas.pack()

ball_1 = Ball(canvas, 1, 1, 50, 1, 0.5, "blue",1)
ball_2 = Ball(canvas, 399, 1, 50, -0.5, 0.5, "red", 1)
ball_3 = Ball(canvas, 201, 191, 50, -0.5, -0.5, "black", 1)
ball_4 = Ball(canvas, 350, 50, 50, 0.5, 0.5, "yellow", 1)
ball_5 = Ball(canvas, 150, 250, 50, -0.5, 0.5, "green", 1)
ball_6 = Ball(canvas, 200, 300, 50, 0.5, -0.5, "purple", 1)
balls = [ball_1, ball_2, ball_3, ball_4, ball_5, ball_6]

while True:
    ball_1.move()
    ball_2.move()
    ball_3.move()
    ball_4.move()
    ball_5.move()
    ball_6.move()
    for i in range(6):
        j = i+1
        while j < 6:
            collision_testing(balls[i], balls[j])
            j+=1
    window.update()
    time.sleep(0.0005)

window.mainloop()