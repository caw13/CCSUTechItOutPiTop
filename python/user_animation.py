from tkinter import *
tk = Tk()

canvas = Canvas(tk, width=500, height=500)
canvas.pack()
shape = canvas.create_polygon(10, 10, 10, 60, 50, 35)

def move_shape(event):
    if event.keysym == 'Up':
        canvas.move(shape, 0, -3)
        canvas.itemconfig(shape,fill="blue")
    elif event.keysym == 'Down':
        canvas.move(shape, 0, 3)
        canvas.itemconfig(shape,fill="red")
    elif event.keysym == 'Left':
        canvas.move(shape, -3, 0)
    else:
        canvas.move(shape, 3, 0)

canvas.bind_all('<KeyPress-Up>', move_shape)
canvas.bind_all('<KeyPress-Down>', move_shape)
canvas.bind_all('<KeyPress-Left>', move_shape)
canvas.bind_all('<KeyPress-Right>', move_shape)
