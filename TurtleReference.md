# Turtle quick reference #
## Getting setup ##
> import turtle

> t = turtle.Pen()

## Basic commands ##
Tell the turtle to move foward/backward a number of steps
> t.forward(50)  
> t.backward(20)  

Tell the turtle to turn a number of degrees
> t.left(90)  
> t.right(180)

Tell the turtle to put its pen up or down
> t.up()
> t.down()  

To clear the canvas and leave turtle where it is
> t.clear()

To clear the canvas and return turtle to its initial state
> t.reset()

### Playing with colors and shapes ###
> t.color("red")

Or can specify value for red, green, blue between 0-255 for each
> t.color()(40,80,120)

Shapes
> t.circle(50)


Or fill shapes like a circle
```
t.begin_fill()
t.circle(10)
t.end_fill()
```

Or your own shapes you create

```
t.reset()
t.color("blue")
t.begin_fill()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.end_fill()
```




Full list of commands reference:
https://docs.python.org/3.0/library/turtle.html
