from numpy import *
import matplotlib.pyplot as mp
n = 9

x = array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = array([14.6, 18.5, 36.6, 30.8, 59.2, 60.1, 62.2, 79.4, 99.9])
mp.plot(x, y, 'ro')
# mp.show()


def g(m, x, c):
    return m*x+c


max = x[0]
min = x[0]

for t in arange(0, n, 1):
    if x[t] > max:
        max = x[t]
    if x[t] < min:
        min = x[t]

mchange = 1
cchange = 1
eps = 1e-2
m = ()
c = 1
chi0 = 0
for i in arange(0, n, 1):
    chi0 += (g(m, x[i], c)-y[i])**2
w = 0
while w < 100:
    chi = 0

    if mchange == 1:
        m += eps
    else:
        m -= eps
    for i in arange(0, n, 1):
        chi += (g(m, x[i], c)-y[i])**2
    if chi > chi0 or chi < chi0:
        if mchange == 1:
            mchange = 2
        else:
            mchange = 1
    chi0 = chi

    if cchange == 1:
        c += eps
    else:
        c -= eps
    for i in arange(0, n, 1):
        chi += (g(m, x[i], c)-y[i])**2
    if chi > chi0 or chi < chi0:
        if cchange == 1:
            cchange = 2
        else:
            cchange = 1
    chi0 = chi

    w += 1

divs = 2
xx = zeros(divs+1)
yy = zeros(divs+1)
for l in arange(0, divs+1, 1):
    xx[l] = min+l*(max-min)/divs
yy = g(m, xx, c)
mp.plot(xx, yy)
mp.show()
