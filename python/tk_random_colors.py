from tkinter import *
import random

def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    color = "#%02x%02x%02x" % (r,b,g)
    return color

tk = Tk()
width = 500
height = 500
canvas = Canvas(tk, width=width, height=height)
canvas.pack()

for i in range (1,10):
    top_left_x = random.randint(0,width)
    top_left_y = random.randint(0,height)
    bottom_left_x = random.randint(top_left_x,width)
    bottom_left_y = random.randint(top_left_y,height)
    canvas.create_rectangle(top_left_x, top_left_y,
                            bottom_left_x,bottom_left_y,
                            fill=random_color())
