from math import cos, sin
import turtle
import numpy as np
from scipy import integrate

wn = turtle.Screen()
wn.title("Double Pendulum")
wn.bgcolor("black")
wn.setup(width=800, height=700)
wn.tracer(0, 0)

m = 1
g = 1
l = 100
a1 = (180.001)*np.pi/180
a2 = (0)*np.pi/180
p1 = 0
p2 = 0
t = .0003
r1 = (l*np.cos(-np.pi/2+a1), l*np.sin(-np.pi/2+a1))
r2 = (l*np.cos(-np.pi/2+a1)+l*np.cos(-np.pi/2+a1+a2),
      l*np.sin(-np.pi/2+a1)+l*np.sin(-np.pi/2+a1+a2))


def bob(r):
    w = turtle.Turtle()
    w.shape('circle')
    w.color('white')
    w.speed(0)
    w.penup()
    w.goto(r)
    w.pendown()
    return w


def arm(r1, r2):
    w = turtle.Turtle()
    w.hideturtle()
    w.speed(0)
    w.color('white')
    w.penup()
    w.goto(r1)
    w.pendown()
    w.goto(r2)
    return w


def adot1(p1, p2, a1, a2):
    return 6/m/l**2*(2*p1-3*cos(a1-a2)*p2)/(16-9*(cos(a1-a2))**2)


def adot2(p1, p2, a1, a2):
    return 6/m/l**2*(8*p2-3*cos(a1-a2)*p1)/(16-9*(cos(a1-a2))**2)


def pdot1(a1, a2, adot1, adot2):
    return -.5*m*l**2*(adot1*adot2*sin(a1-a2)+3*g/l*sin(a1))


def pdot2(a1, a2, adot1, adot2):
    return -.5*m*l**2*(-adot1*adot2*sin(a1-a2)+g/l*sin(a2))


bob1 = bob(r1)
bob2 = bob(r2)
arm1 = arm((0, 0), r1)
arm2 = arm(r1, r2)
i = 0
while True:
    i += 1
    p1 = p1 + t*pdot1(a1, a2, adot1(p1, p2, a1, a2), adot2(p1, p2, a1, a2))
    p2 = p2 + t*pdot2(a1, a2, adot1(p1, p2, a1, a2), adot2(p1, p2, a1, a2))
    a1 = a1 + t*adot1(p1, p2, a1, a2)
    a2 = a2 + t*adot2(p1, p2, a1, a2)
    if i % 4000 == 0:
        r1 = (l*np.cos(-np.pi/2+a1), l*np.sin(-np.pi/2+a1))
        r2 = (l*np.cos(-np.pi/2+a1)+l *
              np.cos(-np.pi/2+a1+a2), l*np.sin(-np.pi/2+a1)+l*np.sin(-np.pi/2+a1+a2))
        bob1.goto(r1)
        bob2.goto(r2)
        arm1.clear()
        arm2.clear()
        arm1 = arm((0, 0), r1)
        arm2 = arm(r1, r2)
        turtle.update()
