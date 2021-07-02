from math import sqrt
import turtle
import operator
import numpy as np

wn = turtle.Screen()
wn.title("2-Body Gravity")
wn.bgcolor("black")
wn.setup(width=1280, height=720)
wn.tracer(0, 0)

r1 = (200, 0)
r2 = (-200, 0)
speed = 0
delta = 0.03

v1 = (0, 7)
v2 = (0, -7)

m1 = 100000
m2 = 100000

mass1 = turtle.Turtle()
mass1.shape("circle")
mass1.color("white")
mass1.penup()
mass1.goto(r1)
mass1.speed(speed)
mass1.pendown()

mass2 = turtle.Turtle()
mass2.shape("circle")
mass2.color("white")
mass2.penup()
mass2.goto(r2)
mass2.speed(speed)
mass2.pendown()

while True:

    r21 = tuple(map(operator.sub, r2, r1))
    r12 = tuple(map(operator.sub, r1, r2))
    r = sqrt(r21[0]**2+r21[1]**2)
    if r < 50:
        r = 50

    v01 = m2*np.array(r21)*delta/r**3
    v1 = tuple(map(operator.add, v1, v01))
    r1 = tuple(map(operator.add, r1, tuple(np.array(v1)*delta)))

    v02 = m1*np.array(r12)*delta/r**3
    v2 = tuple(map(operator.add, v2, v02))
    r2 = tuple(map(operator.add, r2, tuple(np.array(v2)*delta)))

    mass1.goto(r1)
    mass2.goto(r2)
    wn.update()
