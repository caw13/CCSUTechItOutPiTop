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

The next thing we want to add is a way for the user to interact with the ball.  Just like the ball is a class in the game with properties and things it can do, the paddle is going to be the same idea so we are also going to make it a class.  And we will bind the paddle to the user pressing the arrow keys so the paddle moves left or right.
```
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

paddle = Paddle(canvas, 'blue')
```
## ***End of day 3 of camp*** ##
---

# ***You can start at this point with day4_pong.py*** #

https://github.com/caw13/CCSUTechItOutPiTop/blob/master/python/day4_pong.py

---

Next add functionality to our `ball class` so it can check if it hit the paddle.  To do this we need the ball to know about the paddle so modify the top lines of the Ball init method and modify when the ball is created to pass it the paddle:
```
class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        ...
```
```        
ball = Ball(canvas, paddle, 'red')
```
Then add a method to the Ball to see if it is touching the paddle
```
def hit_paddle(self, pos):
    paddle_pos = self.canvas.coords(self.paddle.id)
    # if the ball is between the edges of the paddle...
    if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
        # if the bottom of the ball is between top and bottom of the paddle...
        if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
            return True
    return False
```
Now in the ball's `draw` method where the other position checks are made, add a check to see if it hit the paddle and if so have it go back up
```
if self.hit_paddle(pos) == True:
  self.y = -1
```

### Make the ball stop if it hits the bottom ###
To check if the ball has hit the bottom add a variable to our Ball when we create it
> self.hit_bottom = False

Now when the ball hits the bottom we need to update this variable.  So in the `draw` method where we check if it has hit the bottom, if it has update the variable
```
def draw(self):
  ...
  if pos[3] >= self.canvas_height:
      self.hit_bottom = True
  ...
```
Now in our main method we only want to keep drawing if they haven't hit the bottom so our main loop becomes:
 ```
 while True:
    if not ball.hit_bottom:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
```
## You now have 1 player pong! ##
Now lets add some finishing touches.  Rather than always being the same speed, let's make how fast the ball moves a variable `speed` and let the player decide how fast.

In the creation of Ball in `init` add a new parameter speed that is passed in and a variable self.speed, and use that variable to set the x and y speed
```
class Ball:
    def __init__(self, canvas, paddle, color, speed):
      ...
      self.speed = speed
      self.x = speed
      self.y = -speed
      ...
```

In our draw method where we were updating the speed to be 1 or -1 change these to `self.speed` or `-self.speed` which becomes:
```
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
```

## Now add some interaction with the user ##
So we can interact with the user through the command line or you can interact with them via the graphics elements.
We can create dialog boxes by using `Label`s for the words and `Entry` to take input:
```
dialog = Tk()
name_label = Label(dialog, text="Your name")
name_label.pack()
name_entry = Entry(dialog)
name_entry.pack()
speed_label = Label(dialog, text="Speed")
speed_label.pack()
speed_entry = Entry(dialog)
speed_entry.pack()
speed_entry.insert(0,"1")
```
Then we will add a button as we did in day 3 to tell it to start up our game and put the code to start our game in a function called when the button is picked
```
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
```

The finished program can be seen here:
https://github.com/caw13/CCSUTechItOutPiTop/blob/master/python/one_player_pong.py

# Adding a second player #

So for adding a second player things we want to add:
- A second paddle and controls
- If the ball hits the top it also needs to stop

So if we want to make two paddles, they essentially would be identical in terms of what they did, but we would need to keep track of which controls control which paddle and where each paddle is located.  Turns out we are already doing all of this with our Paddle class, we just need to be able to pass in a different starting position for each paddle and pass in the keys that should control that paddle.
```
class Paddle:
    def __init__(self, position, canvas, color, key_press_left, key_press_right):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, position)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all(key_press_left, self.turn_left)
        self.canvas.bind_all(key_press_right, self.turn_right)

```
Now when we create our paddles we will need to pass a starting position and what keys will control them (and give them different names) and pass both of them to our Ball and have both paddles drawn:
```
bottom_paddle = Paddle(375,canvas, 'green','<KeyPress-Left>','<KeyPress-Right>')
top_paddle = Paddle(30,canvas, 'blue','<KeyPress-1>','<KeyPress-2>')
ball = Ball(canvas, bottom_paddle, top_paddle, 'red', speed)

while True:
    if not ball.hit_bottom:
        ball.draw()
        top_paddle.draw()
        bottom_paddle.draw()
    ...
```

For the Ball we need to now take two paddles
```
class Ball:
    def __init__(self, canvas, bottom_paddle, top_paddle, color, speed):
        self.canvas = canvas
        self.bottom_paddle = bottom_paddle
        self.top_paddle = top_paddle
        ...
```
For handling checking if the ball has hit a paddle we can use our same `hit_paddle` function for both by passing in the paddle as a parameter rather than always being the same paddle
```
def hit_paddle(self, pos, paddle):
    paddle_pos = self.canvas.coords(paddle.id)
    ...
```
Then in the draw method of the Ball update it to check both paddles
```
if self.hit_paddle(pos,self.bottom_paddle) == True:
    self.y = -self.speed
if self.hit_paddle(pos,self.top_paddle) == True:
    self.y = self.speed
```
Finally update it so if the ball hits the top it stops as well

Final code:
https://github.com/caw13/CCSUTechItOutPiTop/blob/master/python/basic_pong.py

# Game enhancements ideas #
- Keep track of points so each time the ball hits the paddle you get a point
- Make your ball speed up each time it hits the paddle
- Add a second ball
- Give the person the ability to start a new game
- Change the ball into an image
- After so many hits add a new block someplace randomly that the ball bounces off of
