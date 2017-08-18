from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
# Draws a line from top left corner (0,0) to bottom right (500,500)
canvas.create_line(0, 0, 500, 500)

# Draw a rectangle first two coordinates are top left corner position,
# second two are bottom right coordinates
canvas.create_rectangle(10,10,300,50)
canvas.create_rectangle(10,10,300,50,fill="blue")

# Draws an arc at position 10,50
# oval would be 200 pixels across, 100 pixels down
# extent is how many degrees of it should be drawn
canvas.create_arc(10, 50, 200, 100, extent=180, style=ARC)
canvas.create_arc(10, 70, 200, 100, extent=230, style=ARC)

# Draw polygon by specifying each point
canvas.create_polygon(10, 10, 100, 10, 100, 110, fill="", outline="black")

# Draw text
canvas.create_text(220, 300, text="Hi John", font=("Arial", 30), fill="blue")
