from tkinter import *
import random
import time



class Ball:
    def __init__(self, canvas, paddle, color, speed):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.speed = speed
        self.x = speed
        self.y = -speed
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = self.speed
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if pos[0] <= 0:
            self.x = self.speed
        if pos[2] >= self.canvas_width:
            self.x = -self.speed
        if self.hit_paddle(pos) == True:
            self.y = -self.speed


    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        # if the ball is between the edges of the paddle...
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            # if the bottom of the ball is between top and bottom of the paddle...
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0



dialog = Tk()

##Label(dialog, text="Your name").grid(row=0)
##Label(dialog, text="Speed").grid(row=1)
##
##name_entry = Entry(dialog).grid(row=0, column=1)
##speed_entry = Entry(dialog).grid(row=1, column=1)
name_label = Label(dialog, text="Your name")
name_label.pack()
name_entry = Entry(dialog)
name_entry.pack()
speed_label = Label(dialog, text="Speed")
speed_label.pack()
speed_entry = Entry(dialog)
speed_entry.pack()
speed_entry.insert(0,"1")

def begin():
    name = "Chad"
    speed = int(speed_entry.get())
    dialog.destroy()
    tk = Tk()
    tk.title("Pong Game")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
    canvas.pack()
    tk.update()
    tk.focus_force()

    paddle = Paddle(canvas, 'blue')
    ball = Ball(canvas, paddle, 'red', speed)

    while True:
        if not ball.hit_bottom:
            ball.draw()
            paddle.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)


btn = Button(dialog, text="Begin", command=begin)
btn.pack()
