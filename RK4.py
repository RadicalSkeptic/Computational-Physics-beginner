from numpy import *

h = 1
y0 = 4.0
x0 = 0.0
x1 = 10.0
tolup = 9e-5
toldwn = 1e-5


def f(a, b):
    return 6*a+11-3*b


def k1(c, d, h):
    return h*f(c, d)


def k2(e, m, h):
    return h*f(e+h/2, m+k1(e, m, h)/2)


def k3(g, j, h):
    return h*f(g+h/2, j+k2(g, j, h)/2)


def k4(k, l, h):
    return h*f(k+h, l+k3(k, l, h))


'''for x in range(x0+h, x1+h, h):
    y = y0+1/6*(k1(x, y0)+2*k2(x, y0)+2*k3(x, y0)+k4(x, y0))
    y0 = y
print(y)'''
x = x0+h
while x < x1+h:
    while True:
        ymin = y0+1/6*(k1(x, y0, h)+2*k2(x, y0, h) +
                       2*k3(x, y0, h)+k4(x, y0, h))
        #ymid = y0+1/6*(k1(x, y0,h)+2*k2(x, y0)+2*k3(x, y0)+k4(x, y0))
        ymax = y0+1/6*(k1(x, y0, h*2)+2*k2(x, y0, h*2) +
                       2*k3(x, y0, h*2)+k4(x, y0, h*2))
        if abs(ymax-ymin) > tolup:
            h /= 2
        elif abs(ymax - ymin) < toldwn:
            h *= 2
            ymin = ymax
            break
        else:
            break

    y0 = ymin
    x += h
print(ymin)
