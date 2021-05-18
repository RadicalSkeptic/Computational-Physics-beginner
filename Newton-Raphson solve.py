from numpy import *

x = 0.5
iter = 1000
eps = 1e-9
h = 1e-3


def func(x):
    return x-tanh(x/.5)


for i in arange(0, iter, 1):
    delx = func(x)*h/(func(x+h)-func(x))

    while abs(func(x-delx)) >= abs(func(x)):
        delx = delx/2

    x = x-delx
    if abs(func(x)) < eps:
        print("\nf(x) = ", func(x), "\nx = ", x)
        break
