from tkinter import Canvas
import math


class Ball:

    def __init__(self, canvas, x, y, diameter, xv, yv, color, mass):
        self.canvas = canvas
        self.xv = xv
        self.yv = yv
        self.diameter = diameter
        self.x=x
        self.y=y
        self.mass = mass
        self.image = canvas.create_oval(x,y,x+diameter,y+diameter, fill=color)


    def move(self):
        corrdinates = self.canvas.coords(self.image)
        if corrdinates[0] <= 0 or corrdinates[2] >= 500:
            self.xv=-self.xv
        if corrdinates[1] <= 0 or corrdinates[3] >= 500:
            self.yv=-self.yv
        self.canvas.move(self.image, self.xv, self.yv)

    def change(self):
        self.xv=-self.xv
        self.yv=-self.yv

    def radius(self):
        return self.diameter/2

    def center(self):
        corrdinates = self.canvas.coords(self.image)
        return (corrdinates[0]+self.diameter/2, corrdinates[1]+self.diameter/2)

    def resultant_velocity(self):
        return math.sqrt(self.xv**2 + self.yv**2)

    def angle(self):
        q = self.xv / self.resultant_velocity()
        return math.acos(q)



class Vector:
    def __init__(self,x,y,xv,yv) -> None:
        self.x=x;
        self.y=y;
        self.xv=xv;
        self.yv=yv;
        self.magnitude, self.theta = self.vector()

    def update(self):
        self.x+=self.xv
        self.y+=self.yv
        self.magnitude, self.theta = self.vector()

    def setXV(self,xv):
        self.xv=xv

    def setYV(self,yv):
        self.yv=yv

    def reverseX(self):
        self.xv=-self.xv

    def reverseY(self):
        self.yv=-self.yv

    def vector(self):
        return (math.sqrt(self.xv**2 + self.yv**2),math.atan2(self.yv,self.xv))

    def triangleSum(self,other):
        theta = math.abs(self.theta-other.theta)
        magnitude = (self.magnitude**2 + other.magnitude**2 -2*self.magnitude*other.magnitude*math.cos(theta))