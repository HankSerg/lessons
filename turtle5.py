from tkinter import *
import turtle

turtle.shape('turtle')
turtle.speed(1)
for i in range(10):
    s = 100+i*10
    # включаем задержку, замедление
    turtle.delay(40)
    turtle.pendown()
    turtle.forward(s)
    turtle.left(90)
    turtle.forward(s)
    turtle.left(90)
    turtle.forward(s)
    turtle.left(90)
    turtle.forward(s)
    turtle.penup()
    # разворот
    turtle.right(45)
    turtle.forward(8)
    turtle.left(135)
