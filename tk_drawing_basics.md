Getting started with loading the graphics package tkinter

```
from tkinter import *
tk = Tk()
```

### Creating buttons ###
Create a button passing it the `tk`, the words for your button, and the function you want it to run when clicked
```
def hello():
    print("hello there")
btn = Button(tk, text="click me", command=hello)
btn.pack()
```

## Drawing with tk using Canvas ##
To create a new drawing/graphics area we create a new `Canvas`
```
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
```
With `turtle` our drawing area coordinates started in the middle of the drawing area.  With `tk` the 0,0 is in the top left
- horizontally as numbers increase it indicates further to right
- vertically as numbers increase it indicates further **down** unlike turtle

A few simple drawing commands:
```
# Draws a line from top left corner (0,0) to bottom right (500,500)
canvas.create_line(0, 0, 500, 500)

# Draw a rectangle first two coordinates are top left corner position,
# second two are bottom right coordinates
canvas.create_rectangle(10,10,300,50)

# Draws an arc at position 10,50
# oval would be 200 pixels across, 100 pixels down
# extent is how many degrees of it should be drawn
canvas.create_arc(10, 50, 200, 100, extent=180, style=ARC)
canvas.create_arc(10, 70, 200, 100, extent=230, style=ARC)

# Draws an oval at position 10,10
# that is 25 wide and 30 tall
canvas.create_oval(10,10,25,25)

# Draw polygon by specifying each point
canvas.create_polygon(10, 10, 100, 10, 100, 110, fill="", outline="black")

# Draw text
canvas.create_text(220, 300, text="Hi John", font=("Arial", 30), fill="blue")
```

## Color ##

With `tk` the color can be a descriptive string like in `turtle` (ex. "blue") or a hex string (ex. "#ef0056").  There is a helper to allow the user to pick a color:
```
canvas.create_rectangle(10, 10, 300, 50, fill="blue")

color = colorchooser.askcolor()
canvas.create_rectangle(10, 10, 300, 50, fill=color[1])
```

If we wanted to create a random color string like we did in turtle we could use this function:
```
def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    # Creates a hex representation of those numbers
    color = "#%02x%02x%02x" % (r,b,g)
    return color

canvas.create_rectangle(10, 10, 300, 50, fill=random_color() )
```
See https://github.com/caw13/CCSUTechItOutPiTop/blob/master/python/tk_random_colors.py

## Loading an image ##
Note the tkinter package can only load ".gif" files.  
```
my_image = PhotoImage(file='field.gif')
canvas.create_image(0,0,anchor=NW, image=my_image)
```

## Basic animation ##
See https://github.com/caw13/CCSUTechItOutPiTop/blob/master/python/basic_animation.py

When you create a shape you can store a reference to it in a variable.  The `canvas.move` method lets you move that shape around the canvas

```
import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
my_shape = canvas.create_polygon(10, 10, 10, 60, 50, 35)

for x in range(0, 60):
    # Tells it to move the shape 5 pixels to the right and 7 pixels down
    canvas.move(my_shape, 5, 7)
    tk.update()
    time.sleep(0.05)
```

## Reacting to the user ##
To make our program able to react to user events like key presses we tell the `canvas` we want to bind to it.  This basically says any time a key is pressed we want to know about it and when it happens call our function.

```
def move_shape(event):
    if event.keysym == 'Up':
        canvas.move(my_shape, 0, -3)

canvas.bind_all('<KeyPress-Up>', move_shape)
```

We can also change the configuration of drawn shapes:
> canvas.itemconfig(shape, fill="blue")

See the code:
https://github.com/caw13/CCSUTechItOutPiTop/blob/master/python/user_animation.py


Reference for keys:
https://docstore.mik.ua/orelly/other/python/0596001886_pythonian-chp-16-sect-9.html
