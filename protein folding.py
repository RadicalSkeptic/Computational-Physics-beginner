from pylab import *
from random import *
import sys

a = 1000
x = [0]
y = [0]


def direc(n):
    l = array([1, 2, 3, 4])
    global x
    global y
    if (x[n] == 30 and y[n] == 40) or (x[n] == 30 and y[n] == -30) or (x[n] == -40 and y[n] == 40) or (x[n] == -40 and y[n] == -30):
        plot(x, y)
        grid(True)
        show()
        sys.exit("corner")
    if x[n] == 30:
        l[0] = 0
    if x[n] == -40:
        l[2] = 0

    if y[n] == 40:
        l[1] = 0
    if y[n] == -30:
        l[3] = 0
    return l


def prox(g):
    k = direc(g)
    global x
    global y
    for q in arange(0, g, 1):
        if (x[g]+1 == x[q]) and (y[g] == y[q]):
            k[0] = 0
        if (x[g] == x[q]) and (y[g]+1 == y[q]):
            k[1] = 0
        if (x[g]-1 == x[q]) and (y[g] == y[q]):
            k[2] = 0
        if (x[g] == x[q]) and (y[g]-1 == y[q]):
            k[3] = 0
    return k


for i in arange(1, a+1, 1):
    f = 0
    d = prox(i-1)
    x.append(x[i-1])
    y.append(y[i-1])
    if d[0] == 0 and d[1] == 0 and d[2] == 0 and d[3] == 0:
        plot(x, y)
        grid(True)
        show()
        sys.exit("no path")
    while f == 0:
        f = choice(d)
        if (f == 1):
            x[i] += 1
        if(f == 2):
            y[i] += 1
        if(f == 3):
            x[i] -= 1
        if(f == 4):
            y[i] -= 1


plot(x, y)
grid(True)
show()
