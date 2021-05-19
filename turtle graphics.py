import turtle as trtl
import tkinter as tk

from numpy import array


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
iter = 10
size = 1
arr = []


def f():
    global c
    global size

    if c == 2:

        bob.fd(size)
        arr.append(0)
        bob.lt(60)
        arr.append(1)
        bob.fd(size)
        arr.append(0)
        bob.rt(120)
        arr.append(2)
        bob.fd(size)
        arr.append(0)
        bob.lt(60)
        arr.append(1)
        bob.fd(size)
        arr.append(0)

    elif c > 2:
        c -= 1
        f()
        bob.lt(60)
        arr.append(1)
        f()
        bob.rt(120)
        arr.append(2)
        f()
        bob.lt(60)
        arr.append(1)
        f()
        c += 1


screen.tracer(0, 0)
a = 0
b = 0
while a == 0:
    if iter == 1:
        bob.fd(size)
        arr.append(0)
        bob.rt(120)
        arr.append(2)
    else:
        c = iter
        f()
        bob.rt(120)
        arr.append(2)
    a += 1

l = len(arr)

while True:
    z = arr[b]
    if z == 0:
        bob.fd(size)
    if z == 1:
        bob.lt(60)
    if z == 2:
        bob.rt(120)
    b += 1
    if b == l:
        b = 0
    if abs(bob.pos()) < 1:
        break
bob.end_fill()
screen.update()
canvas.bind('<MouseWheel>', zoom)

screen.mainloop()
