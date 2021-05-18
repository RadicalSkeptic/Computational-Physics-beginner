import tkinter as tk
from turtle import RawTurtle, TurtleScreen, ScrolledCanvas


def zoom(event):
    amount = 0.9 if event.delta < 0 else 1.1

    canvas.scale(tk.ALL, 0, 0, amount, amount)


root = tk.Tk()

canvas = ScrolledCanvas(master=root, width=2000, height=2000)
canvas.pack(fill=tk.BOTH, expand=tk.YES)

screen = TurtleScreen(canvas)

turtle = RawTurtle(screen)

turtle.penup()
turtle.sety(-250)
turtle.pendown()
turtle.circle(250)

canvas.bind('<MouseWheel>', zoom)

screen.mainloop()
