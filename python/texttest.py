from tkinter import *
tk = Tk()
my_entry = Entry()
my_entry.pack()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

# Draw text
my_text = canvas.create_text(220, 300, text="Hi John", font=("Arial", 30), fill="blue")

def hello():
    name = my_entry.get()
    canvas.itemconfigure(my_text, text=name)

btn = Button(tk, text="click me", command=hello)
btn.pack()
