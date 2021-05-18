from numpy import *

a = -10.0
b = 10.0
eps = 1e-9
divs = 100
iter = 100


def f(x): return x**2 + 2*x - 15


max = b


def bisection(a, b):
    k = 0
    while(k < iter):
        z = (a+b)/2
        k += 1
        if abs(f(a)) < eps:
            print("\nx= ", a)
            break
        if b == max:
            if abs(f(b)) < eps:
                print("\nx= ", b)
                break
        if abs(f(z)) < eps:
            print("\nx= ", z)
            break

        if f(z)*f(a) < 0:
            b = (a+b)/2
        elif f(z)*f(b) < 0:
            a = (a+b)/2
        else:
            break


l = arange(a, b+(b-a)/divs, (b-a)/divs)

for i in arange(0, divs, 1):
    bisection(l[i], l[i+1])
