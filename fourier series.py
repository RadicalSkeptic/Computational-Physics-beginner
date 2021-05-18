import pylab as p
from numpy import *

i = 99  # change this


def fourier(n):
    x = arange(-5, 5, .1)
    y = (((-1)**n)/(n*pi))*sin(n*pi*x)
    return y


y1 = zeros(100)
x = arange(-5, 5, .1)

for n in arange(1, i, 1):
    y1 = y1+fourier(n)
    n += 1

p.plot(x, y1)
p.show()
