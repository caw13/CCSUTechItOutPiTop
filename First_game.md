# Creating our first game #
Basics for our game:
- Animation
- User interaction

## Create our game setup ##
```
from tkinter import *
import random
import time

tk = Tk()
tk.title("Chad's Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
```

## Creating our ball ##

### Classes ###
The idea behind functions was it made it easy to reuse the same functionality over and over.  Here we are going to introduce the idea of a `class` which associates a group of information and functionality together.

With graphics, and games in general, often times the things in the game have particular behaviors.  Using classes allow us to associate all of the information and behavior with that object.

***This goes right after "import time" in the code above***
```
class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

    def draw(self):
        pass  
```
Then our main code at the bottom which just creates an instance of our ball and then has a loop that tells our canvas to keep redrawing
```
ball = Ball(canvas, 'red')

while True:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
```
Now make our ball move every time it is redrawn so modify our draw method inside of Ball:
```
def draw(self):
    self.canvas.move(self.id, 0, -1)
```

### Making the ball bounce ###
Start by telling the ball what direction to start moving and the size of the window by adding these to the `init` method in the ball
```
        self.x = 1
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
```
Then change the draw method to use these and change direction if it reaches the edge of the canvas
```
def draw(self):
    self.canvas.move(self.id, self.x, self.y)
    pos = self.canvas.coords(self.id)
    if pos[1] <= 0:
        self.y = 1
    if pos[3] >= self.canvas_height:
        self.y = -1
    if pos[0] <= 0:
        self.x = 1
    if pos[2] >= self.canvas_width:
        self.x = -1
```

## Adding a paddle ##

# Game enhancements ideas #
- Keep track of points so each time the ball hits the paddle you get a point
- Make your ball speed up each time it hits the paddle
- Add a second ball
- Give the person the ability to start a new game
- Change the ball into an image
