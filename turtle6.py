from tkinter import *
import turtle

""" draw a spider """

turtle.shape('turtle')
turtle.speed(1)
for i in range(12):
    s = 100
    turtle.delay(40)
    turtle.pendown()
    turtle.right(30+30*i)
    turtle.forward(s)
    turtle.stamp()
    turtle.penup()
    turtle.home()
    turtle.penup()
