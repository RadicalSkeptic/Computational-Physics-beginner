from numpy import *


def func(x):
    return 5*(sin(8*x))**2*exp(-x*x)-13*cos(3*x)


def trapezoid(a, b, n):
    h = (b-a)/(n-1)
    sum = (func(a)+func(b))/2
    for i in range(1, n-1):
        sum += func(a+i*h)
    return h*sum


a = .5
b = 2.3
n = 12000
print(trapezoid(a, b, n-1))
