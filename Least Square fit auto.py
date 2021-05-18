from numpy import *
import matplotlib.pyplot as mp
import scipy.optimize as so
x = array([1, 1.1, 1.24, 1.35, 1.451, 1.5, 1.92])
y = array([.52, .8, .7, 1.8, 2.9, 2.9, 3.6])
n = 7
mp.plot(x, y, 'ro')
# mp.show()


def g(x, a1, a2, a3):
    return a1+a2*x+a3*x**2


para, cova = so.curve_fit(g, x, y)
print(para)

a1 = para[0]
a2 = para[1]
a3 = para[2]
max = x[0]
min = x[0]

for t in arange(0, n, 1):
    if x[t] > max:
        max = x[t]
    if x[t] < min:
        min = x[t]


divs = 1000
xx = zeros(divs+1)
yy = zeros(divs+1)
for l in arange(0, divs+1, 1):
    xx[l] = min+l*(max-min)/divs
yy = g(xx, a1, a2, a3)
mp.plot(xx, yy)
mp.show()
