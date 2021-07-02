import turtle
import operator
from math import sqrt
import numpy as np
from time import sleep

wn = turtle.Screen()
wn.title("n-Body Gravity(click on screen)")
wn.bgcolor("black")
wn.setup(width=1280, height=720)
wn.tracer(0, 0)
wn.screensize(12800, 7200)

m = 100000
t = .02
thresh = 40
mass = []


def body(x, y):
    w = turtle.Turtle()
    w.shape('circle')
    w.color('white')
    w.speed(0)
    w.penup()
    w.goto(x, y)
    return w


def r(r1, r2):
    return tuple(map(operator.sub, r2, r1))


def rd(r):
    return sqrt(r[0]**2+r[1]**2)


def v0(v0, r, rd):
    return tuple(map(operator.add, m*np.array(r)*t /
                     rd**3, v0))


def v(v, v0):
    return tuple(map(operator.add, v, v0))


def pos(r, v):
    return tuple(map(operator.add, r, tuple(np.array(v)*t)))


def append(x, y):
    mass.append(body(x, y))


vn = [(0, 10), (0, -10), (0, 0)]
mass.append(body(200, 0))
mass.append(body(-200, 0))
mass.append(body(0, 0))
z = 0
while True:
    wn.update()
    z += 1
    wn.onscreenclick(append)
    n = len(mass)
    x = len(vn)
    while n > x:
        vn.append((0, 0))
        x = len(vn)
    i = 0
    for a in range(len(mass)):
        r1 = mass[a].pos()
        v01 = (0, 0)
        for b in range(len(mass)):
            if a == b:
                continue
            r2 = mass[b].pos()
            r21 = r(r1, r2)
            rd12 = rd(r21)
            if rd12 < thresh:
                rd12 = thresh
            v01 = v0(v01, r21, rd12)
        vn[i] = v(vn[i], v01)
        r1 = pos(r1, vn[i])
        i += 1
        mass[a].goto(r1)
