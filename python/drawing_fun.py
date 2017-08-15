import turtle
import random


def circle(x, y, size):
    t = turtle.Pen()
    t.setpos(x,y)
    t.color(random.random(),random.random(),random.random())
    t.begin_fill()
    t.circle(size)
    t.end_fill()

circle(30)
circle(50)
circle(70)
