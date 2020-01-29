from tkinter import *
import turtle
import math
""" move turtle to draw circle """

a = (math.pi*140.00/360)

turtle.shape('turtle')

for i in range(1,361,1):
    turtle.left(a)
    turtle.forward(1)
