from numpy import *


def f(x):
    return 2*cos(x)-x


def bisection(xminus, xplus, nmax, eps):
    for it in range(0, nmax):
        x = (xplus+xminus)/2
        print(" it ", it, " x ", x, "f(x)", f(x))
        if (f(xplus)*f(x) > 0):
            xplus = x
        else:
            xminus = x
        if abs(f(x)) < eps:
            print("\nRoot found with precision= ", eps)
            break
        if it == nmax-1:
            print("\nRoot NOT found after nmax iterations")
    return x


eps = 1e-6
a = 0.0
b = 5.0
imax = 100
root = bisection(a, b, imax, eps)
print("Root= ", root)
