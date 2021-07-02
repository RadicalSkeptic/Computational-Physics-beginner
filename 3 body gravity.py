from math import sqrt
import turtle
import operator
import numpy as np
from time import sleep

wn = turtle.Screen()
wn.title("3-Body Gravity")
wn.bgcolor("black")
wn.setup(width=1280, height=720)
wn.tracer(0, 0)
wn.screensize(12800, 7200)
r1 = (100, 0)
r2 = (-100, 0)
r3 = (0, 100)

delta = .01
m1 = 10000
m2 = 10000
m3 = 10000

v1 = (0, 10)
v2 = (0, -10)
v3 = (0, 0)
speed = 0


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

mass3 = turtle.Turtle()
mass3.shape("circle")
mass3.color("white")
mass3.penup()
mass3.goto(r3)
mass3.speed(speed)
mass3.pendown()
i = 0
thresh = 40
while True:

    r21 = tuple(map(operator.sub, r2, r1))
    r12 = tuple(map(operator.sub, r1, r2))
    r13 = tuple(map(operator.sub, r1, r3))
    r23 = tuple(map(operator.sub, r2, r3))
    r31 = tuple(map(operator.sub, r3, r1))
    r32 = tuple(map(operator.sub, r3, r2))

    rd12 = sqrt(r12[0]**2+r12[1]**2)
    if rd12 < thresh:
        rd12 = thresh
    rd13 = sqrt(r13[0]**2+r13[1]**2)
    if rd13 < thresh:
        rd13 = thresh
    rd23 = sqrt(r23[0]**2+r23[1]**2)
    if rd23 < thresh:
        rd23 = thresh

    v01 = tuple(map(operator.add, m2*np.array(r21)*delta /
                rd12**3, m3*np.array(r31)*delta/rd13**3))
    v1 = tuple(map(operator.add, v1, v01))
    r1 = tuple(map(operator.add, r1, tuple(np.array(v1)*delta)))

    v02 = tuple(map(operator.add, m1*np.array(r12)*delta /
                rd12**3, m3*np.array(r32)*delta/rd23**3))
    v2 = tuple(map(operator.add, v2, v02))
    r2 = tuple(map(operator.add, r2, tuple(np.array(v2)*delta)))

    v03 = tuple(map(operator.add, m2*np.array(r23)*delta /
                rd23**3, m1*np.array(r13)*delta/rd13**3))
    v3 = tuple(map(operator.add, v3, v03))
    r3 = tuple(map(operator.add, r3, tuple(np.array(v3)*delta)))

    mass1.goto(r1)
    mass2.goto(r2)
    mass3.goto(r3)
    if i % 100 == 0:
        wn.update()
    i += 1
