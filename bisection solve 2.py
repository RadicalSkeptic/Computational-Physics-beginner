from numpy import *

a = 0.5
b = 1.5
eps = 1e-9


def f(x): return x-tanh(x/.5)


while(1):
    z = (a+b)/2

    if f(a) == 0:
        print("x = ", a)
        exit()
    if f(b) == 0:
        print("x = ", b)
        exit()
    if abs(a-b) < eps:
        print("x = ", z)
        exit()

    if f(z)/abs(f(z)) != f(a)/abs(f(a)):
        b = (a+b)/2
    elif f(z)/abs(f(z)) != f(b)/abs(f(b)):
        a = (a+b)/2
    else:
        print("Sign doesn't change between ", a, " and ", b)
        exit()
