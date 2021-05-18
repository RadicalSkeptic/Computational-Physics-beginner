import turtle as trtl
import tkinter as tk


def zoom(event):
    amount = 0.9 if event.delta < 0 else 1.1

    canvas.scale(tk.ALL, 0, 0, amount, amount)


root = tk.Tk()

canvas = trtl.ScrolledCanvas(master=root, width=20000, height=20000)
canvas.pack(fill=tk.BOTH, expand=tk.YES)

screen = trtl.TurtleScreen(canvas)

bob = trtl.RawTurtle(screen)
bob.color("red", "yellow")
bob.begin_fill()
bob.speed(0)
iter = 5
size = 1


def f():
    global c
    global size

    if c == 2:

        bob.fd(size)
        bob.lt(60)
        bob.fd(size)
        bob.rt(120)
        bob.fd(size)
        bob.lt(60)
        bob.fd(size)

    elif c > 2:
        c -= 1
        f()
        bob.lt(60)
        f()
        bob.rt(120)
        f()
        bob.lt(60)
        f()
        c += 1


while True:
    if iter == 1:
        bob.fd(size)
        bob.rt(120)
    else:
        c = iter
        f()
        bob.rt(120)
    if abs(bob.pos()) < 1:
        break

bob.end_fill()
canvas.bind('<MouseWheel>', zoom)

screen.mainloop()
